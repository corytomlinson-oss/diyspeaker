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
5. Mean Well EPS-65-24-C enclosed Class I power supply (24 V, 2.71 A).

The PSU is Class I, so the IEC earth must be bonded to the chassis. Signal ground stays separate.

## Drivers

| Role | Part | Key specs | Price |
|---|---|---|---|
| Woofer | Dayton ND91-4 (3.5" full-range) | Fs 74 Hz, Qts 0.41, Vas 1.4 L, Xmax 4.6 mm, 82.4 dB at 1 W / 1 m, 30 W RMS | $27.98 |
| Tweeter | Dayton ND25FA-4 (1" soft dome) | Fs 1,350 Hz, Qts 1.56, 90 dB at 2.83 V, 20 W RMS, flat above 3 kHz | $11.49 |

**Crossover:** 4th-order Linkwitz-Riley at about 2.5 to 3 kHz, set in DSPi. Start at 3 kHz. The 3.5" woofer will be near its limit at 2.5 kHz, and the tweeter's usable range starts at 2.5 kHz.

**Previously considered:**
- MAC-04 (4" midrange): Dropped for the 3.5" ND91-4. Its official datasheet was not accessible, and its Xmax (3 mm, from the overhang figure) was lower than the ND91-4's 4.6 mm.
- SB12NRXF25-4 (4"): Discontinued from the standard range (OEM only, MOQ 100).
- Tang Band W4-1720 (4"), Dayton SIG120-4 (4"), SB12PACR25-4 (4"): Viable, but larger than the reference box.
- Dayton TD25F-4 (1" tweeter, about $23): Replaced by the ND25FA-4 at lower cost.
- ND20FB-4 (¾" tweeter, about $14): Usable, but its Fs (1.7 to 2.1 kHz) and lower power rating made the ND25FA-4 the better fit.

## Cost (per speaker, estimate)

| Item | Cost |
|---|---|
| Woofer, ND91-4 | $27.98 |
| Tweeter, ND25FA-4 | $11.49 |
| Electronics (ADC, Pico 2, DAC, amp, PSU) | ~$84 |
| Filament and misc. hardware (IEC inlet, RCA jack, wire, fasteners, damping) | ~$20–35 |
| **Total** | **~$130–145** |

For the pair: roughly $260 to $290 before shipping and tax. The filament and misc. line is an estimate.

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
- WinISD not yet run for the ND91-4. Hand calculation at 1.5 L sealed: Qtc about 0.57, −3 dB about 103 Hz.

## Open items

1. WinISD sealed-box run at 1.5 L with the ND91-4 parameters.
2. CAD enclosure at about 165 × 114 × 127 mm, with the internal volume checked and the driver cutouts placed.
3. Confirm the ND91-4 and ND25FA-4 cutout diameters from the official drawings. The ND25FA-4 is listed at Ø45 mm, and the ND91-4's cutout isn't confirmed.
4. Confirm the ND25FA-4 frequency response and the ND91-4 response in the box with measurements.
5. Check the EPS-65 and PCM1808 board dimensions against the enclosure.
6. TPA3116D2 input sensitivity and DSPi output gain, to avoid clipping.
7. Crossover check with measurements, and tweeter level match.

## Sources

- ND91-4: loudspeakerdatabase.com listing and Parts Express (price).
- ND25FA-4: Parts Express listing (specs and price).
- Passive Aggressive Mini kit (box size reference): Parts Express.
- TPA3116D2 board: Parts Express (price).
- PCM5102 DAC: Adafruit (price).
- Raspberry Pi Pico 2: Core Electronics (price).
- PCM1808 board: Fruugo (price, currency not confirmed).
- EPS-65-24-C: TRC Electronics (price).
- Bambu Lab X1C build volume: MakeItLabs wiki (256 × 256 × 256 mm).
- DSP: WeebLabs DSPi (github.com/WeebLabs/DSPi).

Hand calculations are estimates. Confirm them in WinISD and by measurement before building.
