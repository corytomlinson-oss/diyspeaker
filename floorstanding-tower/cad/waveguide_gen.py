"""
Parametric waveguide generator — 2.5-way tower project.
Wavecor TW030WA05 front-mount overlay.

v2: superellipse-morphed OS profile (Tritonia-inspired rounded-rect mouth).
    Set se_n = 2.0 and equal W/H to get the old round waveguide back.

Outputs: waveguide.stl, testfit_ring.stl, profile.png (+ console drill data)

PRINT NOTES (Bambu X1C, 256 mm bed — 9.00 x 7.75" part fits flat):
  Mouth (big face) DOWN. 0.12 mm layers, 5-6 walls, 40% gyroid, PETG/ASA.
  Pocket ceiling (top of print) is a flat annular bridge: allow supports
  there or accept minor sag (non-acoustic back side).
  Acoustic surface finish: filler primer + 400 grit.

ALL PARAMETERS IN INCHES. Edit block below, rerun, reprint.
"""
import numpy as np
from stl import mesh

IN = 25.4

# ------------------------- PARAMETERS (edit me) -------------------------
throat_dia_in   = 1.850   # 46.25 mm measured surround OD + 0.75 mm clearance
relief_ri_in    = 1.02    # pocket-floor relief groove for the 3 proud
relief_ro_in    = 1.65    # faceplate Torx heads (annulus, non-acoustic)
relief_d_in     = 0.09
os_half_angle   = 65.0    # OS asymptote (deg from axis); coverage near
                          # crossover is set mostly by mouth size
mouth_w_in      = 8.00    # flare outline (where roundover meets face), W
mouth_h_in      = 6.75    # ... and H  (aspect ~0.84, Tritonia-like)
se_n            = 3.7     # superellipse exponent: 2=ellipse, ~3.7=rounded rect
part_w_in       = 9.00    # flange outline W (fits X1C bed)
part_h_in       = 7.75    # flange outline H
flange_n_boost  = 1.3     # flange outline slightly boxier than mouth
roundover_in    = 0.75    # mouth terminating roundover (reference radius)
pocket_dia_in   = 4.59    # 115 mm faceplate + 0.6 mm clearance
pocket_depth_in = 0.20    # MEASURED 4.25 mm plate + ~0.8 mm foam preload
n_screws        = 4       # at the four corners (45 deg diagonals)
seg_around      = 256
seg_profile     = 100
# -----------------------------------------------------------------------

rt = throat_dia_in/2*IN
rri, rro, rd = relief_ri_in*IN, relief_ro_in*IN, relief_d_in*IN
R  = roundover_in*IN
rp = pocket_dia_in/2*IN
zp = pocket_depth_in*IN
theta = np.radians(os_half_angle); tan_t = np.tan(theta)

def se_radius(phi, A, B, n):
    """Radius of superellipse |x/A|^n+|y/B|^n=1 along azimuth phi."""
    c, s = np.abs(np.cos(phi)), np.abs(np.sin(phi))
    return ((c/A)**n + (s/B)**n) ** (-1.0/n)

# --- reference (round) profile built on the geometric-mean mouth radius ---
a_m, b_m = mouth_w_in/2*IN, mouth_h_in/2*IN
rm_ref = np.sqrt(a_m*b_m)
r1   = rm_ref - R*np.sin(theta)              # OS ends, roundover begins
z_os = np.sqrt(r1**2 - rt**2)/tan_t
zs   = np.linspace(0, z_os, seg_profile)
os_r = np.sqrt(rt**2 + (zs*tan_t)**2)
Pz, Pr = zp + z_os, r1                        # roundover arc, tangent to OS
Cz, Cr = Pz - R*np.sin(theta), Pr + R*np.cos(theta)
aa    = np.linspace(theta, np.pi/2, 24)[1:]
arc_z = Cz + R*np.sin(aa); arc_r = Cr - R*np.cos(aa)
z_top = arc_z[-1]
ref_r = np.concatenate([os_r[1:], arc_r])     # radial part that morphs
ref_z = np.concatenate([zp + zs[1:], arc_z])  # depths (fixed for all phi)

# --- morph: throat stays circular, mouth follows the superellipse ---
ang = np.linspace(0, 2*np.pi, seg_around, endpoint=False)
A_o, B_o = part_w_in/2*IN, part_h_in/2*IN
profiles = []
for phi in ang:
    rm_phi = se_radius(phi, a_m, b_m, se_n)
    s      = (rm_phi - rt)/(rm_ref - rt)      # radial scale for this azimuth
    ro_phi = se_radius(phi, A_o, B_o, se_n + flange_n_boost)
    pr = rt + (ref_r - rt)*s
    prof = [(ro_phi, 0.0), (rp, 0.0), (rp, zp), (rro, zp),
            (rro, zp+rd), (rri, zp+rd), (rri, zp), (rt, zp)] \
         + list(zip(pr, ref_z)) + [(ro_phi, z_top)]
    profiles.append(np.array(prof))
profiles = np.array(profiles)                 # (seg_around, P, 2)

# --- sweep into watertight binary STL ---
def sweep(profs, fname):
    n, P = profs.shape[0], profs.shape[1]
    verts = np.empty((n, P, 3))
    for i in range(n):
        a = 2*np.pi*i/n
        verts[i, :, 0] = profs[i, :, 0]*np.cos(a)
        verts[i, :, 1] = profs[i, :, 0]*np.sin(a)
        verts[i, :, 2] = profs[i, :, 1]
    faces = []
    for i in range(n):
        j = (i+1) % n
        for k in range(P):
            k2 = (k+1) % P
            faces.append([verts[i, k], verts[j, k2], verts[j, k]])
            faces.append([verts[i, k], verts[i, k2], verts[j, k2]])
    m = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    m.vectors[:] = np.array(faces)
    m.save(fname)
    return m

sweep(profiles, "waveguide.stl")

# --- test-fit ring (circular pocket, unchanged) ---
ringp = np.array([(rp+0.5*IN, 0.0), (rp, 0.0), (rp, zp), (rro, zp),
                  (rro, zp+rd), (rri, zp+rd), (rri, zp), (rt, zp),
                  (rt, zp+rd+2.0), (rp+0.5*IN, zp+rd+2.0)])
sweep(np.repeat(ringp[None, :, :], 128, axis=0), "testfit_ring.stl")

# --- drawing: plan view + H/V cross-sections ---
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
ph = np.linspace(0, 2*np.pi, 400)
for A, B, n, lbl in [(a_m, b_m, se_n, "mouth flare"),
                     (A_o, B_o, se_n+flange_n_boost, "part outline")]:
    rr = se_radius(ph, A, B, n)
    ax1.plot(rr*np.cos(ph)/IN, rr*np.sin(ph)/IN, label=lbl)
ax1.add_patch(plt.Circle((0, 0), rt/IN, fill=False, ls="--", color="gray"))
ax1.set_aspect("equal"); ax1.legend(fontsize=8); ax1.grid(alpha=.3)
ax1.set_title("plan view (in)")
for idx, lbl in [(0, "horizontal"), (seg_around//4, "vertical")]:
    p = profiles[idx]
    ax2.plot(p[:, 1]/IN, p[:, 0]/IN, label=lbl)
ax2.set_aspect("equal"); ax2.legend(fontsize=8); ax2.grid(alpha=.3)
ax2.set_xlabel("depth (in)"); ax2.set_ylabel("radius (in)")
ax2.set_title("cross-sections")
plt.tight_layout(); plt.savefig("profile.png", dpi=130)

# --- console summary + drill template ---
print(f"Part: {part_w_in:.2f} x {part_h_in:.2f}\", total depth {z_top/IN:.2f}\" "
      f"(flare {z_os/IN:.2f}\" + pocket {zp/IN:.2f}\")")
print(f"Mouth flare {mouth_w_in:.2f} x {mouth_h_in:.2f}\" (n={se_n}), "
      f"throat {throat_dia_in:.2f}\", roundover {roundover_in:.2f}\"")
phc = np.pi/4
r_in  = (rt + (ref_r[-1]-rt)*(se_radius(phc, a_m, b_m, se_n)-rt)/(rm_ref-rt))
r_out = se_radius(phc, A_o, B_o, se_n+flange_n_boost)
r_scr = 0.5*(r_in + r_out)
print(f"Corner screws: {n_screws}x at r = {r_scr/IN:.2f}\" on 45-deg diagonals:")
for i in range(n_screws):
    a = np.pi/4 + i*np.pi/2
    print(f"   screw {i+1}: x = {r_scr*np.cos(a)/IN:+.3f}\", "
          f"y = {r_scr*np.sin(a)/IN:+.3f}\"")
print("Drill after printing (7/64\" pilot in baffle, countersink part) "
      "or add negative cylinders in Bambu Studio.")
