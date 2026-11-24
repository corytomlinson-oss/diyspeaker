# Parts List: Studio Monitors (pair)

Quantities are for the pair (two speakers) unless noted. Prices are from the checks noted below and change often, so confirm before ordering. "Verify" means the item hasn't been fully checked yet.

Status key: **Chosen** = decided, **Verify** = needs a check before ordering.

## Drivers and audio electronics

| Item | Qty | Price (approx.) | Where | Status |
|---|---|---|---|---|
| Peerless SLS-85S25CP04-04 woofer (3.5", 4 Ω) | 2 | $21.00 each | [Parts Express](https://www.parts-express.com/Peerless-SLS-85S25CP04-04-3-1-4-Paper-Cone-Woofer-4-Ohm-264-1600?quantity=1) (back-ordered about 2 weeks) | Chosen. Datasheet on file. |
| Peerless by Tymphany XT25SC40-04 tweeter (1" ring radiator, faceplate-free, 4 Ω) | 2 | $18.00 each | [Parts Express 264-1642](https://www.parts-express.com/Peerless-XT25SC40-04-1-Ring-Radiator-XT-Tweeter-4-Ohm-264-1642?quantity=1) | Chosen. Spec sheet on file. Replaced the ND25FN-4 (out of stock). |
| PCM1808 ADC module | 2 | Not verified | Amazon listing (link not saved) | Verify the input filter before use (see `pcm1808-board-test.md`) |
| Raspberry Pi Pico 2 | 2 | ~$5 each | Not verified | Verify |
| PCM5102 I2S DAC breakout (Adafruit 6250 listing) | 2 | $4.95 each | [Adafruit](https://www.adafruit.com/product/6250) | Chosen |
| TPA3116D2 stereo amp board (2 × 50 W) | 2 | $13.98 each | [Parts Express](https://parts-express.com/TPA3116D2-2x50W-Class-D-Stereo-Amplifier-Board-with-Volume-Control-320-699) (back-ordered) | Chosen |

## Power

| Item | Qty | Price (approx.) | Where | Status |
|---|---|---|---|---|
| Mean Well IRM-60-24ST PSU (24 V, 2.5 A, 60 W, screw terminals, Class II) | 2 | About $17.30 each (Master Electronics listing, USD) | Master Electronics (link not saved). Digi-Key 1866-3068-ND is listed with a 17-week lead time, so it is not the first choice. | Chosen. Datasheet on file. Verify stock and price before ordering. |
| Traco Power TSR 3-2450N, 24 V to 5 V buck module (3 A) | 2 | $12.53 each (CAD, Digi-Key Canada) | [Digi-Key (Canada)](https://www.digikey.ca/en/products/detail/traco-power/TSR-3-2450N/25903120) | Chosen. Check the US Digi-Key page for USD pricing. |
| Panel-mount IEC C14 inlet with switch and fuse holder, 1 to 2 mm panel (Qualtek/Mean Well 723W-BEL3BR51A) | 2 | Not checked | Digi-Key: search "723W-BEL3BR51A" | Chosen. Unchanged by the PSU switch: the speaker still needs a mains inlet, switch, and fuse holder. Datasheet on file. Verify the Digi-Key listing. |
| Bel Fuse 5HT 2-R, 2 A slow-blow, 5×20 mm, 250 V | 4 | Not checked | [Digi-Key 5923-5HT2-R-ND](https://www.digikey.com/en/products/detail/bel-fuse-inc/5ht-2-r/1008982) | Chosen. Two per speaker. |
| IEC C14 power cord (US, 3-prong) | 2 | Not checked | Digi-Key or local | Verify. The IRM-60 is Class II, so the cord's earth pin is not used by the PSU. A 3-prong cord is still the normal choice. |

## Wiring and connectors

| Item | Qty | Notes | Status |
|---|---|---|---|
| 18 AWG stranded wire, red, black, and green | 1 roll each | Mains live and neutral (inlet to PSU), 24 V and ground runs. Green is only needed if you bond the inlet's earth terminal to something. | Verify |
| Ring or spade terminals for the IRM-60 screw terminals, sized for 18 AWG, with insulating sleeves | 1 kit | Mains L and N into the PSU, DC +24 V and −V out. | Verify |
| Panel-mount RCA jack | 2 | One per speaker. Buying from Amazon. | Chosen (source: Amazon) |
| Driver gasket tape (thin foam) | 1 roll | Seals the woofer and tweeter to the printed baffle so the sealed box doesn't leak. | Have it already |
| Shielded signal wire, 24 AWG | 1 roll | RCA to ADC, DAC to amp | Verify |
| Spade terminals, 0.187" with insulating sleeves | 1 kit | Speaker connections | Verify |
| 2.54 mm headers (female and male) | 1 set | Pico and boards | Verify |
| Dupont jumper wires (female-to-female) | 1 pack | Testing I2S connections | Verify |
| Heat shrink tubing | 1 assortment | All crimped joints | Verify |

## Not on Digi-Key, or needs a local source

- Polyfill or fiberfill (damping), local hardware or craft store
- M3 standoffs and screws, local hardware store (check the IRM-60 mounting holes and fit inside the box)
- Insulating sheet (Mylar or similar) under the PSU, only if the mounting surface is conductive
- 3D printing filament (PLA or PETG), about $5 to $10 per box
- Cable gland or strain relief for the mains cable, optional

## Measurement gear (one-time)

| Item | Price (approx.) | Notes |
|---|---|---|
| miniDSP UMIK-1 calibrated measurement mic | About $140 at Parts Express (free shipping, 15% coupon) | Ordering with the drivers and amps. Download the 0-degree calibration file by serial number. |
| 3.5 mm to RCA cable | Local | Computer output to the speaker's RCA input for REW sweeps |
| USB audio interface, 2-in / 2-out (Behringer UMC202HD) | $50 to $70 | Optional, buy later if needed. Adds a loopback timing reference, impedance measurements, and direct electronics measurements. |
| Multimeter | ~$20 | Resistance and voltage |
| Mic stand and tape measure | Local | |
| REW and WinISD | Free | Software |

## Open checks before ordering

1. PCM1808 module: confirm the input network on the board (see `pcm1808-board-test.md`).
2. Source, stock, and USD price for the IRM-60-24ST (Master Electronics or another non-Digi-Key seller).
3. Digi-Key listing and stock for the 723W-BEL3BR51A inlet.
4. US Digi-Key pricing for the TSR 3-2450N.
5. Raspberry Pi Pico 2 source and price.
6. Wire and terminal part numbers (screw-terminal ferrules, 18 AWG).
7. Peerless cutout diameter (drawing appears to show about Ø86.5 mm) and XT25SC40-04 front diameter (about Ø44 mm) and depth (about 20.8 mm body, 32.6 mm overall), read from a small drawing.
8. Confirm 3D-printed panel or insert for the inlet (1 to 2 mm thick, required by the 723W).
9. Confirm the IRM-60-24ST mounting method and footprint (screw-terminal version is 109 × 52 × 33.5 mm) fits the enclosure.
