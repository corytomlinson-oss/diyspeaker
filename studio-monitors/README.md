# DIY Active Studio Monitors

A pair of DIY two-way active studio monitors, inspired by the Genelec 4020C. Each speaker is self-contained: power cord, one RCA input, and everything else inside the box.

## Goals

- All electronics inside each speaker, including the power supply. Each speaker needs only a power cord and one RCA cable.
- Analog input, so the speakers work with a record player as well as a computer.
- DSP crossover, EQ, and level control via WeebLabs DSPi on a Raspberry Pi Pico 2.
- Outside envelope no larger than the SB Acoustics Micro-C box: 262 × 132 × 170 mm. Smaller is better.
- Walls about 1/2 inch (12.7 mm).

## Signal chain (per speaker)

1. RCA input into a PCM1808 stereo ADC (one per speaker).
2. Pico 2 running DSPi: matrix mixing, PEQ, crossover, delay, output gain.
3. Stereo I2S DAC, one channel per driver.
4. TPA3116D2 class D amplifier, one channel per driver, 26 dB gain.
5. Mean Well EPS-65-24-C enclosed Class I power supply (24 V, 2.71 A).

The PSU is Class I, so the IEC earth must be bonded to the chassis. Signal ground stays separate.

## Drivers (current status)

| Role | Part | Status |
|---|---|---|
| Woofer | MAC-04 (Midwest Audio Club, 4") | Provisional. About $20. Testing one in the box before committing to a pair. |
| Tweeter | Dayton TD25F-4 | Tentative. Fs 900 Hz, 91 dB, 20 W RMS. Not yet checked against the MAC-04. |

Earlier woofer candidate: SB12NRXF25-4. Discontinued from the standard range (OEM only, MOQ 100). Not chosen.

## Enclosure

- Sealed box. The MAC-04 manufacturer's recommended box is a 5.7 L vented design, which doesn't fit the envelope. Sealed was chosen for this reason.
- Internal gross volume with 1/2-inch walls: about 3.6 L. Target net volume after driver displacement, bracing, and electronics: about 2.6 L.
- Mounting: MAC-04 cutout Ø98 mm (per the mounting drawing; measure before cutting), flange Ø121 mm, bolt circle Ø110 mm, 4 × Ø4.5 mm holes, 60.5 mm depth behind a 5 mm flange.

## Status

- Design phase. No measurements yet.
- WinISD model not yet run. Hand calculations for MAC-04 at 2.6 L sealed: Qtc about 0.76, −3 dB about 111 Hz.

## Open items

1. Official MAC-04 datasheet: Xmax (listed as "Xmax overhang" of 3 mm, which isn't the same), and the meaning of the 50 W asterisk. The OneDrive link from the Midwest Audio Club page is not accessible.
2. WinISD sealed-box run at 2.6 L with MAC-04 parameters.
3. Net volume after the driver, bracing, and PSU/amp/boards are placed.
4. Crossover to TD25F-4 (LR4 near 2.5 kHz) and level match (about 4 dB tweeter pad), confirmed by measurement.
5. TPA3116D2 input sensitivity and DSPi output gain, to avoid clipping.
6. Baffle layout and orientation of the 262 × 132 × 170 mm envelope.

## Sources

- Mounting and frequency data: Midwest Audio Club MAC-04 drawing and specification sheet.
- Woofer specifications used for comparison: SB Acoustics, Dayton Audio, Tang Band, and Peerless listings and spec sheets.
- Amplifier: TPA3116D2 class D stereo amplifier board.
- Power supply: Mean Well EPS-65-24-C.
- DSP: WeebLabs DSPi (github.com/WeebLabs/DSPi).

Hand calculations are marked as estimates. Confirm them in WinISD and by measurement before building.
