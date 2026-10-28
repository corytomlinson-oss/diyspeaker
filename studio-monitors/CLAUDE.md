# CLAUDE.md: studio-monitors

Context for Claude working in this folder. Read this before making changes.

## What this project is

A DIY two-way active studio monitor built by Cory, inspired by the Genelec 4020C. Each speaker has its own PCM1808 ADC, Pico 2 running DSPi, I2S DAC, TPA3116D2 class D amp, and EPS-65-24-C PSU. The full design rationale is in README.md.

## Hard constraints (do not change without asking)

- Outside envelope: no larger than 262 × 132 × 170 mm. Smaller is better.
- Walls: about 1/2 inch (12.7 mm).
- Everything inside the box, including the PSU. Users connect only power and one RCA cable.
- Analog input, so the speakers work with a record player.
- Sealed enclosure. The port and passive radiator options were ruled out because the box is too small for a usable port tuning.

## Working conventions

- Label every calculated number as an estimate or hand calculation unless it's from a manufacturer datasheet or a measurement.
- Cite sources for driver specs. Note when a value is missing, like Xmax, rather than guessing silently.
- Keep units explicit: mm, L, Hz, Ω, Tm, dB.
- Don't present WinISD results as if they were run unless the output is actually provided. WinISD runs on Windows, and Cory runs it locally.
- Don't claim a driver is in stock or in production without a current source. Parts status changes.

## Current state

- Woofer: MAC-04 (provisional, about $20). The SB12NRXF25-4 was discontinued from the standard range (OEM only, MOQ 100) and is not used.
- Tweeter: Dayton TD25F-4 (tentative).
- Enclosure: sealed, net volume target about 2.6 L.
- Open: MAC-04 official datasheet (Xmax, 50 W asterisk), WinISD run, crossover and level match, amp input level, baffle layout.

## Files

- README.md: project overview, design decisions, and open items. Keep this current when decisions change.
- CLAUDE.md: this file.

Add new files (calculations, WinISD exports, measurement logs) as separate files in this folder, not inside README.md.
