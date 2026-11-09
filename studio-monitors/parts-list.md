# Parts List: Studio Monitors (pair)

Quantities are for the pair (two speakers) unless noted. Prices are from the checks noted below and change often, so confirm before ordering. "Verify" means the item hasn't been fully checked yet.

Status key: **Chosen** = decided, **Verify** = needs a check before ordering.

## Drivers and audio electronics

| Item | Qty | Price (approx.) | Where | Status |
|---|---|---|---|---|
| Peerless SLS-85S25CP04-04 woofer (3.5", 4 Ω) | 2 | $21.00 each | [Parts Express](https://www.parts-express.com/Peerless-SLS-85S25CP04-04-3-1-4-Paper-Cone-Woofer-4-Ohm-264-1600?quantity=1) (back-ordered about 2 weeks) | Chosen. Datasheet on file. |
| Dayton ND25FN-4 tweeter (1" silk dome, faceplate-free) | 2 | $11.00 each | Parts Express (link not saved) | Chosen |
| PCM1808 ADC module | 2 | Not verified | Amazon listing (link not saved) | Verify the input filter before use (see `pcm1808-board-test.md`) |
| Raspberry Pi Pico 2 | 2 | ~$5 each | Not verified | Verify |
| PCM5102 I2S DAC breakout (Adafruit 6250 listing) | 2 | $4.95 each | [Adafruit](https://www.adafruit.com/product/6250) | Chosen |
| TPA3116D2 stereo amp board (2 × 50 W) | 2 | $13.98 each | [Parts Express](https://parts-express.com/TPA3116D2-2x50W-Class-D-Stereo-Amplifier-Board-with-Volume-Control-320-699) (back-ordered) | Chosen |

## Power

| Item | Qty | Price (approx.) | Where | Status |
|---|---|---|---|---|
| Mean Well EPS-65-24-C PSU (24 V, 2.71 A, enclosed) | 2 | $18.10 each (Digi-Key) | [Digi-Key 1866-1721-ND](https://www.digikey.com/en/products/detail/mean-well-usa-inc/EPS-65-24-C/7703204?s=N4IgTCBcDaIKIAcDOBaAbAVhWALCgxiALoC%2BQA) | Chosen |
| Traco Power TSR 3-2450N, 24 V to 5 V buck module (3 A) | 2 | $12.53 each (CAD, Digi-Key Canada) | [Digi-Key (Canada)](https://www.digikey.ca/en/products/detail/traco-power/TSR-3-2450N/25903120) | Chosen. Check the US Digi-Key page for USD pricing. |
| Panel-mount IEC C14 inlet with switch and fuse holder, 1 to 2 mm panel | 2 | Not checked | Digi-Key: search "723W-BEL3BR51A" | Chosen. Datasheet on file. Verify the Digi-Key listing. |
| Bel Fuse 5HT 2-R, 2 A slow-blow, 5×20 mm, 250 V | 4 | Not checked | [Digi-Key 5923-5HT2-R-ND](https://www.digikey.com/en/products/detail/bel-fuse-inc/5ht-2-r/1008982) | Chosen. Two per speaker. |
| IEC C14 power cord (US, 3-prong) | 2 | Not checked | Digi-Key or local | Verify |

## Wiring and connectors (Digi-Key and Amazon)

| Item | Qty | Notes | Status |
|---|---|---|---|
| JST VH cable assemblies, 3-position (PSU AC input) and 4-position (PSU DC output), 18 AWG | 4 (2 of each) | Pre-made leads from Amazon, so no crimping. Match the PSU's B3P-VH and B4P-VH connectors. | Verify length, wire gauge, and that they're VH series |
| 18 AWG stranded wire, red, black, and green | 1 roll each | Mains (green earth), 24 V and ground runs | Verify |
| Ring terminals for M3 screws (earth) | 4 | For PSU screws M1 and M2 | Verify |
| Panel-mount RCA jack | 2 | One per speaker | Verify |
| Shielded signal wire, 24 AWG | 1 roll | RCA to ADC, DAC to amp | Verify |
| Spade terminals, 0.187" with insulating sleeves | 1 kit | Speaker connections | Verify |
| 2.54 mm headers (female and male) | 1 set | Pico and boards | Verify |
| Dupont jumper wires (female-to-female) | 1 pack | Testing I2S connections | Verify |
| Heat shrink tubing | 1 assortment | All crimped joints | Verify |

## Not on Digi-Key, or needs a local source

- Polyfill or fiberfill (damping), local hardware or craft store
- M3 standoffs and screws, local hardware store
- Mylar film insulator sheet, for the PSU mounting
- 3D printing filament (PLA or PETG), about $5 to $10 per box
- Cable gland or strain relief for the mains cable, optional

## Measurement gear (one-time)

| Item | Price (approx.) | Notes |
|---|---|---|
| miniDSP UMIK-1 calibrated measurement mic | $75 to $90 | Includes a calibration file |
| USB audio interface, 2-in / 2-out (Behringer UMC202HD) | $50 to $70 | |
| Multimeter | ~$20 | Resistance and voltage |
| Mic stand and tape measure | Local | |
| REW and WinISD | Free | Software |

## Open checks before ordering

1. PCM1808 module: confirm the input network on the board (see `pcm1808-board-test.md`).
2. Digi-Key listing and stock for the 723W-BEL3BR51A inlet.
3. US Digi-Key pricing for the TSR 3-2450N.
4. Raspberry Pi Pico 2 source and price.
5. Wire, connector, and crimp tool part numbers on Digi-Key.
6. Peerless cutout diameter (drawing appears to show about Ø86.5 mm) and ND25FN-4 cutout (Ø41 mm per datasheet).
7. Confirm 3D-printed panel or insert for the inlet (1 to 2 mm thick, required by the 723W).
