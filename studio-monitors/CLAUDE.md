# CLAUDE.md: studio-monitors

Context for Claude working in this folder. Read this before making changes.

## What this project is

A DIY two-way active studio monitor built by Cory as a learning project, inspired by the Genelec 4020C and kept as cheap as practical. Each speaker has its own PCM1808 ADC, Pico 2 running DSPi, PCM5102 DAC, TPA3116D2 class D amp, and EPS-65-24-C PSU. The enclosure is 3D-printed on a Bambu Lab X1C. The full design rationale is in README.md.

## Hard constraints (do not change without asking)

- Enclosure must print on the X1C as one piece: longest side at or below about 230 mm (build volume 256 × 256 × 256 mm).
- Everything inside the box, including the PSU. Users connect only power and one RCA cable.
- Analog input, so the speakers work with a record player.
- Sealed enclosure. Port and passive radiator options were ruled out.
- Learning project and cheap: prefer low-cost parts and simple builds, and say so when a choice costs more.

## Working conventions

- Label every calculated number as an estimate or hand calculation unless it's from a manufacturer datasheet or a measurement.
- Cite sources for driver specs. Note when a value is missing, like Xmax or a cutout diameter, rather than guessing silently.
- Keep units explicit: mm, L, Hz, Ω, Tm, dB.
- Don't present WinISD results as if they were run unless the output is actually provided. WinISD runs on Windows, and Cory runs it locally.
- Don't claim a driver is in stock or in production without a current source. Parts status changes.
- Parts prices are listing prices from the date they were checked. Re-check before purchase.
- Some data sources have errors. The ND20FB-4 data package readme referenced a different model, and its Fs disagreed with the spec sheet. Flag such conflicts instead of picking one silently.

## Current state

- Woofer: Dayton ND91-4 (3.5" full-range), $27.98.
- Tweeter: Dayton ND25FA-4 (1" soft dome), $11.49.
- Crossover: LR4 at about 2.5 to 3 kHz, starting at 3 kHz, in DSPi.
- Enclosure: sealed, 3D-printed, reference size about 165 × 114 × 127 mm, net volume target about 1.5 L.
- Estimated cost: about $130 to $145 per speaker.
- Open: WinISD run at 1.5 L, CAD enclosure, ND91-4 and ND25FA-4 cutout diameters, board dimensions, amp input level and DSPi output gain, crossover measurements.
- Measurement gear to buy: UMIK-1 mic, USB interface, multimeter, mic stand. REW and WinISD are free.

## Files

- README.md: project overview, design decisions, costs, and open items. Keep this current when decisions change.
- CLAUDE.md: this file.

Add new files (calculations, WinISD exports, measurement logs, CAD notes) as separate files in this folder, not inside README.md.
