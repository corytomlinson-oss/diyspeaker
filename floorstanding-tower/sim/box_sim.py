import numpy as np

# Multicomp Pro 55-5670 T/S (per driver)
Fs, Qts, Qes, Vas_L = 36.1, 0.32, 0.424, 58.85
QL = 7.0  # box loss

def vented_response(f, Vb_L, Fb):
    """4th-order vented box HF-normalized response (per driver in Vb)."""
    a = Vas_L / Vb_L            # alpha
    h = Fb / Fs                 # tuning ratio
    Ts = 1/(2*np.pi*Fs)
    Tb = 1/(2*np.pi*Fb)
    s = 1j*2*np.pi*f
    # Standard Thiele/Small 4th order polynomial (with leakage QL)
    num = (s**4)*(Ts**2)*(Tb**2)
    den = (s**4)*(Ts**2)*(Tb**2) \
        + (s**3)*(Tb**2*Ts/Qts + Ts**2*Tb/QL) \
        + (s**2)*((a+1)*Tb**2 + Tb*Ts/(QL*Qts) + Ts**2) \
        + s*(Tb/QL + Ts/Qts) + 1
    return 20*np.log10(np.abs(num/den))

f = np.logspace(np.log10(15), np.log10(200), 300)

candidates = [
    ("25 L @ 38 Hz (small/QB3)", 25, 38),
    ("32 L @ 33 Hz (balanced)",  32, 33),
    ("40 L @ 30 Hz (extended)",  40, 30),
    ("50 L @ 27 Hz (max ext.)",  50, 27),
]

for name, vb, fb in candidates:
    r = vented_response(f, vb, fb)
    # F3, F6, F10
    def fx(db):
        idx = np.where(r >= -abs(db))[0]
        return f[idx[0]] if len(idx) else None
    # ripple/peaking check above 40 Hz
    peak = r.max()
    print(f"{name}: F3={fx(3):.1f} Hz  F6={fx(6):.1f} Hz  F10={fx(10):.1f} Hz  peak={peak:+.2f} dB")

# refine + export chart data for two finalists
f2 = np.logspace(np.log10(20), np.log10(200), 25)
for name, vb, fb in [("A: 28 L @ 36 Hz", 28, 36), ("B: 35 L @ 31 Hz", 35, 31)]:
    r = vented_response(f2, vb, fb)
    print(name, "|", ",".join(f"{x:.1f}" for x in r))
    rfull = vented_response(f, vb, fb)
    idx3 = np.where(rfull >= -3)[0]; idx6 = np.where(rfull >= -6)[0]
    print(f"   F3={f[idx3[0]]:.1f} F6={f[idx6[0]]:.1f}")

# Port check: 100mm dia port, Vb total 70 L, Fb 31
import math
Sd = 211e-4; Xmax = 7.5e-3; Vd = 2*Sd*Xmax
for d_cm, Fb, VbT in [(10.2, 31, 70), (7.62, 31, 70)]:
    Av = math.pi*(d_cm/2)**2  # cm^2
    v = Vd*2*math.pi*Fb/(Av*1e-4)
    Lv = (23562.5*d_cm**2)/(Fb**2*VbT) - 0.732*d_cm
    print(f"port d={d_cm}cm: velocity@Fb≈{v:.1f} m/s, length≈{Lv:.1f} cm")
