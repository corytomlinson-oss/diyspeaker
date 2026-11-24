# DIY Active Studio Monitors

A learning project: a pair of small DIY two-way active studio monitors, inspired by the Genelec 4020C and kept as cheap as practical. Each speaker is self-contained: power cord, one RCA input, and everything else inside a 3D-printed box.

## Goals

- All electronics inside each speaker, including the power supply. Each speaker needs only a power cord and one RCA cable.
- Analog input, so the speakers work with a record player as well as a computer.
- DSP crossover, EQ, and level control via WeebLabs DSPi on a Raspberry Pi Pico 2.
- Enclosure printed on a Bambu Lab X1C (256 × 256 × 256 mm build volume) as a single piece, with no split parts.
- Lowest practical cost. This is a learning build, so the goal is to see what can be done.

## Enclosure

- **Print limits:** Keep the longest side at or below about 230 mm, leaving margin for brims and warping. The Micro-C envelope (262 mm long) no longer applies because it won't fit the X1C.
- **Reference size:** About 165 × 114 × 127 mm outside, based on the Passive Aggressive Mini kit. Final dimensions to be set in CAD.
- **Walls:** 4 to 6 mm printed walls with internal ribs and damping. The earlier 1/2-inch (12.7 mm) wall target was for wood and is no longer used.
- **Type:** Sealed. The port and passive radiator options were ruled out: a port tuned to a useful frequency needs a tube longer than the box, and a radiator adds parts and tuning work we don't need yet.
- **Volume:** Target about 1.5 L net after driver displacement, bracing, and electronics. With 5 mm walls, the gross internal volume at the reference size is about 1.9 L.
- **Stiffness:** Printed plastic rings more than MDF. Use ribs and damping material to keep resonance down.

## Signal chain (per speaker)

1. RCA input into a PCM1808 stereo ADC (one per speaker).
2. Pico 2 running DSPi: matrix mixing, PEQ, crossover, delay, output gain.
3. Stereo I2S DAC (PCM5102 class), one channel per driver.
4. TPA3116D2 class D amplifier (2 × 50 W board), one channel per driver, 26 dB gain.
5. Mean Well IRM-60-24ST screw-terminal Class II power supply (24 V, 2.5 A, 60 W, single output).

The PSU is Class II (no FG pin), so it needs no earth bond to the enclosure. The panel inlet's earth terminal is not used by the PSU. Signal ground stays separate. The PSU was switched from the EPS-65-24-C (Class I, JST connectors, 2.71 A) to the IRM-60-24ST: it has screw terminals, lower ripple (150 mVp-p vs 240 mVp-p), and is easier to source outside Digi-Key. Its 2.5 A output is slightly below the EPS-65's 2.71 A, which is still enough for this design.

## Drivers

| Role | Part | Key specs | Price |
|---|---|---|---|
| Woofer | Peerless SLS-85S25CP04-04 (3.5" paper cone) | Fs 72.6 Hz, Qts 0.35, Vas 1.39 L, Xmax 4.5 mm, 83.3 dB at 1 W / 1 m, 86.0 dB at 2.83 V, 30 W RMS | $21.00 |
| Tweeter | Peerless by Tymphany XT25SC40-04 (1" ring radiator, faceplate-free) | Fs 1,018 Hz (±15%), Qts 0.63, Re 3.22 Ω, Zmin 3.79 Ω, Le 0.01 mH, Sd 8 cm², Xmax 0.1 mm, 91.1 dB at 2.83 V, 87.9 dB at 1 W / 1 m, 100 W rated noise power. Front about Ø44 mm, body about 20.8 mm behind the mounting face, about 32.6 mm overall including the phase plug (read from a small drawing, confirm on the part). | $18.00 |

The tweeter is locked in for a baffle-mounted waveguide. It ships without a faceplate for custom mounting. Its "central waveguide" is the bullet-shaped phase plug in the middle of the ring diaphragm, not an outer flare, so the whole waveguide is still ours to design; the throat must clear the phase plug. The Voz Pacifica build (a4eaudio.com) uses this tweeter in a Visaton WG 148 R waveguide, which shows the approach works. Xmax is tiny (0.1 mm, normal for ring radiators), so keep the crossover at about 3 kHz and don't go much below 2.5 kHz. The tweeter is about 5 dB more sensitive than the woofer, so attenuate it in DSPi. At 91 dB, amp hiss may be audible near-field; lower the TPA3116D2 gain setting if so.

**Crossover:** 4th-order Linkwitz-Riley at about 2.5 to 3 kHz, set in DSPi. Start at 3 kHz (about 3× the tweeter's Fs). The 3.5" woofer will be near its limit at 2.5 kHz, and the tweeter's tiny Xmax sets a floor around 2.5 kHz.

**Previously considered:**
- Dayton ND91-4 (3.5" full-range, $27.98): Very close on paper to the Peerless, but about $7 more per speaker. Replaced by the Peerless.
- MAC-04 (4" midrange): Dropped for the 3.5" ND91-4. Its official datasheet was not accessible, and its Xmax (3 mm, from the overhang figure) was lower than the ND91-4's 4.6 mm.
- SB12NRXF25-4 (4"): Discontinued from the standard range (OEM only, MOQ 100).
- Tang Band W4-1720 (4"), Dayton SIG120-4 (4"), SB12PACR25-4 (4"): Viable, but larger than the reference box.
- Dayton ND25FN-4 (1" silk dome, $11): The previous choice. Replaced by the XT25SC40-04 because it went out of stock for a long time. The XT25 also has a lower Fs (1,018 vs 1,350 Hz) and far higher power handling (100 W vs 20 W), at $7 more per speaker.
- Dayton TD25F-4 (1" tweeter, about $23): Replaced by the ND25FA-4 at lower cost.
- ND20FB-4 (¾" tweeter, about $14): Usable, but its Fs (1.7 to 2.1 kHz) and lower power rating made the ND25FA-4 the better fit.

## Cost (per speaker, estimate)

| Item | Cost |
|---|---|
| Woofer, Peerless SLS-85S25CP04-04 | $21.00 |
| Tweeter, XT25SC40-04 | $18.00 |
| Electronics (ADC, Pico 2, DAC, amp, PSU) | ~$52 |
| Filament and misc. hardware (IEC inlet, RCA jack, wire, fasteners, damping) | ~$20–35 |
| **Total** | **~$111–126** |

For the pair: roughly $222 to $252 before shipping and tax. The tweeter switch to the XT25SC40-04 added $7 per speaker. An earlier version of this table counted the MAC-04 woofer twice, so the total was overstated by about $20 per speaker. This corrects it. The filament and misc. line is an estimate.

## Measurement gear (to purchase)

- **Calibrated measurement mic:** miniDSP UMIK-1 (roughly $75 to $90). The calibration file ships with each unit.
- **USB audio interface:** 2 in / 2 out, such as the Behringer UMC202HD (roughly $50 to $70).
- **REW (Room EQ Wizard):** free. Frequency response, impedance, distortion, and gating.
- **Multimeter:** for resistance and wiring checks.
- **Mic stand and tape measure:** for consistent 1 m on-axis placement.
- **WinISD:** free, for box modeling.
- **Thiele-Small measurement:** not essential. REW doesn't extract Thiele-Small parameters directly, and the manufacturer values are close enough for this design.

Prices are rough. Verify before purchase.

## Status

- Design phase. Drivers and electronics locked in. Enclosure not yet designed.
- No measurements yet.
- WinISD not yet run for the Peerless. Hand calculation at 1.5 L sealed: Qtc about 0.49, −3 dB about 101 Hz.
- Waveguide for the tweeter is being considered for the baffle. Not designed yet.

## Open items

1. WinISD sealed-box run at 1.5 L with the Peerless parameters.
0a. Test the PCM1808 board's input filter (static and functional). Step-by-step guide: studio-monitors/pcm1808-board-test.md.
1a. Design the baffle waveguide for the XT25SC40-04: throat matched to the ring diaphragm and clearing the phase plug, mouth size for a 3 kHz crossover, and a mounting method (printed clamp ring, bolted plate, or glued pocket).
2. CAD enclosure at about 165 × 114 × 127 mm, with the internal volume checked and the driver cutouts placed.
3. Confirm the Peerless woofer cutout and the XT25SC40-04 front diameter (about Ø44 mm) and depths on the actual parts. The Peerless drawing appears to show about Ø86.5 mm, which is hard to read and needs confirming. The Peerless is about 76 mm deep, so check that it leaves room for the amp and PSU inside the box.
3a. Decide whether the tweeter gets a waveguide, and if so design it into the baffle, with time alignment in DSPi.
4. Confirm the XT25SC40-04 response in the waveguide and the woofer response in the box with measurements.
5. Check the IRM-60-24ST (109 × 52 × 33.5 mm, screw-terminal version) and PCM1808 board dimensions against the enclosure.
6. TPA3116D2 input sensitivity and DSPi output gain, to avoid clipping.
7. Crossover check with measurements, and tweeter level match.

## Sources

- Peerless SLS-85S25CP04-04: Tymphany driver spec sheet (attached PDF, rev 1, 2017), Parts Express (price, $21 from user).
- ND91-4: loudspeakerdatabase.com listing and Parts Express (price).
- XT25SC40-04: Tymphany driver spec sheet (attached PDF, rev 1, 2017-03-03), Parts Express (price, $18 from user). Voz Pacifica design, a4eaudio.com (waveguide use reference).
- Passive Aggressive Mini kit (box size reference): Parts Express.
- TPA3116D2 board: Parts Express (price).
- PCM5102 DAC: Adafruit (price).
- Raspberry Pi Pico 2: Core Electronics (price).
- PCM1808 board: Fruugo (price, currency not confirmed).
- Mean Well IRM-60-24ST: Mean Well IRM-60 spec sheet (attached PDF, 2025-11-21), Master Electronics listing (about $17.30 USD, price to re-check).
- Bambu Lab X1C build volume: MakeItLabs wiki (256 × 256 × 256 mm).
- DSP: WeebLabs DSPi (github.com/WeebLabs/DSPi).

Hand calculations are estimates. Confirm them in WinISD and by measurement before building.
