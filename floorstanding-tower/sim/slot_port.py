import math
c = 343.0
Fb = 31.0
Vb = 0.070  # m^3 net
W_int = 0.244   # internal width, slot spans full width
for h_mm in [30, 35, 40]:
    S = W_int * h_mm/1000.0
    L_acoustic = c*c*S/(4*math.pi**2*Fb**2*Vb)
    d_eff = math.sqrt(4*S/math.pi)
    # end corrections: inner end flanged (~0.425*d), outer end in baffle (~0.425*d) -> ~0.85*d total
    L_phys = L_acoustic - 0.85*d_eff
    v = (2*211e-4*7.5e-3)*2*math.pi*Fb/S  # port velocity at full excursion
    print(f"slot {W_int*1000:.0f} x {h_mm} mm: area {S*1e4:.0f} cm2, physical length {L_phys*100:.1f} cm, v@Fb {v:.1f} m/s, aspect {W_int*1000/h_mm:.1f}:1")
