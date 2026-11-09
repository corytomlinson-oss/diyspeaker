# 2.5-Way Tower Speaker Project

A DIY 2.5-way floorstanding speaker using two 8" woofers and a waveguide-loaded 30mm dome tweeter.

## Status

**WOOFER DECIDED (Aug 18, 2026): Dayton RS225-8.** Enclosure redesigned as slim tower (below). Waveguide print-ready pending test-fit ring.
Next: measurement school + gear list, test-fit ring print, then order woofers & verify T/S before cutting wood.

## Drivers

| Position | Driver | Notes |
|---|---|---|
| Woofers (x2) | Dayton Audio RS225-8, 8" (Parts Express 295-378) | Reference Series, black anodized aluminum cone, cast frame |
| Tweeter (x1) | Wavecor TW030WA05 (Cinergy Audio buyout, #98-027) | 30mm textile dome, 4 ohm, no ferrofluid, chambered rear |
| Waveguide | Custom 3D-printed OS, superellipse (rounded-rect) mouth 8" × 6.75" (9" × 7.75" part) | Front-mount over 4.53" faceplate; X1C one-piece |

### Woofer key parameters (Dayton RS225-8, from datasheet — re-verify at order time)

- Fs: 28.3 Hz, Qts: 0.38, Vas: 2.01 ft³ (56.8 L)
- Xmax: 0.28" (7 mm), Sd ≈ 33.1 in² (213.8 cm²); pair displacement ~299 cc
- Sensitivity: 86.8 dB / 2.83V/1m, 80 W RMS
- Frame OD 8.78", cutout 7.24", depth 3.5"
- Fully documented: factory curves + Klippel + extensive 3rd-party measurements; proven in ~1.8–2 kHz designs
- Aluminum cone: known ~5 kHz breakup peak → small LCR notch in UPPER woofer low-pass (lower/.5 woofer needs none)

### Tweeter key parameters (TW030WA05)

- Fs: 450 Hz (exceptionally low — enables low crossover); no ferrofluid → tall undamped impedance peak at Fs
- Recommended range: 1.5–25 kHz; power handling 50 W (IEC, 2 kHz @ 12 dB/oct)
- Sensitivity: 91.5 dB (2.83V/1m) — ~1.5 dB above woofer before waveguide gain → L-pad required
- Rdc: 3.4 Ω (4-ohm nominal), Le: 20 µH, Sd: 11.5 cm², Qt 0.59 (Qm 1.5 / Qe 0.96)
- Faceplate per Wavecor outline drawing (needed for waveguide interface)

## Architecture: 2.5-Way Rationale

- 8" woofer beams above ~1.5–2 kHz → crossover must be low (~1.6–1.9 kHz)
- Wavecor's 450 Hz Fs + waveguide loading gain (~3–6 dB in 1.5–4 kHz) makes a 1.6–1.9 kHz LR4 crossover safe
- Waveguide matches tweeter directivity to woofer directivity at crossover → smooth off-axis / power response
- Lower woofer low-passed ~300–450 Hz (first-order-ish) for baffle-step compensation → system sensitivity ~87 dB (non-issue with Hypex NCx252MP headroom)
- Bass impedance: two 8 Ω woofers in parallel → ~4 Ω minimum. Amp must be 4-ohm stable.

## Enclosure & Baffle Spec (SLIM TOWER v2 — FINAL pending T/S verification of delivered RS225-8s)

| Parameter | Value |
|---|---|
| Alignment | Vented, ~1.6 ft³ net per speaker (both woofers shared volume), Fb = 28 Hz |
| Predicted response | F3 ≈ 43 Hz anechoic, F6 ≈ 34 Hz, F10 ≈ 27 Hz — beats old 2.2 ft³ Multicomp design everywhere |
| Port | **Slot port, front bottom: 9.5" × 1" opening; L-fold path ~17" total** (≈8-3/4" along bottom + ≈8-1/2" up rear wall; build vertical leg 1" long and trim to tune); ~8.6 m/s max (silent); round over lips and fold |
| External dims | **11" W × 11" D × 39" H**, 3/4" MDF/ply, + 1.5–2" plinth recommended (tweeter height) or ~2° back-tilt |
| Internal dims | 9.5" × 9.5" × 37.5" ≈ 1.96 ft³ gross → ~1.62 ft³ net (drivers, port, bracing/xover deductions) |
| Baffle edges | 1" radius roundovers, full height, front vertical edges |
| Driver centers (from cabinet bottom) | Tweeter 34-1/4", upper woofer 25-7/8" (8-3/8" CTC — RS225 frame is 8.78" OD), lower woofer 14-1/8" (11-3/4" CTC) |
| Woofer cutouts | 7.24" dia (per Dayton drawing — verify on delivered units) |
| Bracing | Window braces ~9" / 20.5" / 30.5" (dodge drivers + port fold); optional magnet-to-rear brace |
| Damping | Wall lining ~1" (no loose stuffing), heavier in top half; keep port path clear |
| Crossover mount | Bottom chamber, accessible via removable panel or lower woofer hole |
| Baffle step | ~410 Hz (11" baffle) → .5 woofer low-pass target |
| Tweeter crossover | ~1.6–1.9 kHz LR4 (acoustic) |
| .5 woofer low-pass | ~400 Hz, first order electrical (expect ~5–6 mH iron core) |
| Upper woofer low-pass | LR4-target ~1.7–1.9 kHz + LCR notch at ~5 kHz cone breakup |
| System sensitivity | ~87 dB / 2.83V (amp headroom: 21 dB — see System Context) |
| Nominal impedance | 4 Ω |

Simulation code: `sim/box_sim.py` (alignments), `sim/slot_port.py` (port sizing). History: original Multicomp design was 11 × 14 × 39" / 2.2 ft³ @ 33.5 Hz; RS225-8 gives deeper bass in 21% less volume.

## Open Decisions

1. Waveguide throat: measure actual dome opening diameter (~1.5" nominal) and dome recess depth on delivered tweeters before finalizing STL
2. Verify measured T/S of actual woofers before cutting wood (adjust Fb / shelf length if needed)
3. Woofer cutout diameter — measure actual drivers (datasheet omits it; ~7-1/4" typical)

## Resolved Decisions

- Woofer: **Dayton RS225-8** (Aug 18, 2026) — chosen from 18-candidate survey for best price/performance: matches compact-box bass champions (F3 43 Hz in 1.6 ft³) while being the only budget option fully documented through our 1.7–1.9 kHz crossover region (factory + Klippel + 3rd-party data, proven designs). ~$270/four. Known cost: ~5 kHz aluminum breakup → notch in upper woofer LP; 86.8 dB sensitivity (moot given amp). Runners-up: Satori MW19P-8 (best quality, 2.8x price), Epique E180HE-44 (deepest bass, subwoofer-class motor unproven at our crossover). Multicomp 55-5670 dropped: credible forum testimony caps it ~800–900 Hz with dome tweeters — incompatible with our topology.
- Tweeter variant: **TW030WA05** (4 ohm, no ferrofluid) — Cinergy Audio buyout. 91.5 dB sensitivity gives L-pad headroom over waveguide gain.
- Enclosure: **SLIM TOWER 11 × 11 × 39", ~1.6 ft³ net vented @ 28 Hz**, front slot port 9.5" × 1" with L-fold (~17" path) — supersedes the 11 × 14 × 39" Multicomp design (Aug 18, 2026)
- Crossover: **passive**. 4-ohm tweeter values; L-pad on tweeter; likely LCR trap at 450 Hz Fs peak (no ferrofluid); .5 section ~5–6 mH iron core
- Waveguide: **OS profile morphed to a superellipse (rounded-rect) mouth** — Tritonia-inspired (at-horns.eu), front-mount overlay over the 115 mm (4.53") faceplate. Geometry: 1.5" throat (nominal, pending calipers), 65° OS asymptote, mouth flare 8" × 6.75" (n=3.7 superellipse, ~0.84 aspect), 3/4" roundover, part 9" × 7.75" × 1.74" deep (1.35" flare + 0.32" pocket + 0.07" roundover rise). Rationale: non-round mouth spreads mouth-edge diffraction across frequency (smoother on-axis); flat-ish sides ease baffle mounting (4 corner screws at ±3.14", ±3.14"); shorter vertical dimension gives clearance at the 8-1/4" tweeter-woofer CTC. Round version recoverable via se_n=2 + equal W/H. NOTE: our morph borrows the Tritonia concept, not its BEM-optimized geometry — verify coverage/ripple by measurement in Phase 4. Mounting: **front screws through the four solid corners** — #8 × 2.5" into baffle pilots at ±3.14"/±3.14", countersunk (or Bambu Studio negative-part holes); foam gasket tape on back face (air seal) and on pocket floor (faceplate preload, anti-buzz). Front removal keeps the captive tweeter serviceable. Generator: `cad/waveguide_gen.py` v2. One-piece X1C print (229 × 197 mm footprint): mouth-down, 0.12 mm layers, 5–6 walls, 40% gyroid, PETG/ASA, filler-primer + sand. Print test-fit ring first.

## Project Phases

1. **Baffle layout & enclosure sizing** — box volume, port, driver placement, baffle width
2. **Box modeling** — vented alignment sim (T/S based), port velocity check
3. **Waveguide design** — profile geometry, 3D print, throat interface to Wavecor faceplate
4. **Measurement** — raw driver responses on final baffle (REW + calibrated mic)
5. **Crossover design** — from measured data (VituixCAD or DSP)
6. **Build, verify, voice**

## To Purchase (list to be finalized next session)

- Woofers: 4x Dayton RS225-8 (Parts Express 295-378, ~$67 ea — confirm price)
- Measurement gear: calibrated USB mic, impedance-jig parts, calipers — full list with tutorial next session
- Waveguide mounting: #8 x 2.5" screws (8), foam gasket tape, countersink bit
- Crossover parts: after measurement phase (don't buy yet; includes ~5 kHz notch LCR for upper woofers)
- Wood, port/terminal hardware, damping, filament (PETG or ASA): after T/S verification

## Risks

- RS225-8 ~5 kHz breakup must be notched in the upper woofer low-pass — well-documented fix, verify by measurement
- Verify measured T/S of delivered woofers before cutting wood (Dayton QC is good but confirm)
- Waveguide throat mismatch to dome geometry can cause 10–15 kHz ripple — iterate prints
- L-fold port adds a bend: round over the fold edge and both lips to keep it silent
