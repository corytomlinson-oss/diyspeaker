# CLAUDE.md — Speaker Project Context

## What this project is

Step-by-step design of a 2.5-way floorstanding speaker (pair). The owner wants to design collaboratively with Claude, one phase at a time, documenting decisions as we go.

## Ground rules for Claude

- **The owner is completely new to speaker design and is using this project as a learning experience.** For every new topic: explain the basics first and WHY we're doing it, then the specifics. Define jargon on first use. Don't assume prior audio knowledge.
- Work step by step; don't jump ahead of the current phase without asking
- Update README.md whenever a decision is made or a phase completes (Status, Open Decisions, targets)
- Show the math/reasoning behind acoustic recommendations, not just conclusions
- Prefer designing from measured data over datasheet data wherever possible; flag when we're relying on unverified datasheet numbers
- All build dimensions IMPERIAL (inches, ft³, lb). Keep Hz/ohm/dB and metric driver model names (e.g., 30mm dome). Stock is 3/4" sheet.

## Fixed decisions (do not revisit unless asked)

- Topology: 2.5-way, passive crossover
- Woofers: 2x Dayton RS225-8 (8", 8 Ω, aluminum cone) — DECIDED Aug 18, 2026; T/S in README.md; needs ~5 kHz notch in upper woofer LP
- Tweeter: Wavecor TW030WA05 (4 Ω, no ferrofluid; Cinergy Audio buyout #98-027)
- Tweeter gets a custom 3D-printed OS waveguide: front-mount overlay over 115 mm faceplate, ~1.5" throat / 7" mouth / ~1.5" deep, printed one-piece on user's Bambu X1C (256 mm bed)
- Crossover target: ~1.6–1.9 kHz LR4 acoustic to tweeter

## Current phase

PAUSED (Aug 3, 2026) after completing Phase 0 (feasibility), Phase 1 (enclosure/baffle/slot port — spec in README), and waveguide concept decisions. Sim code: sim/box_sim.py (alignments), sim/slot_port.py (port).

## Agenda for next session (owner requested)

1. **Teach: how to measure drivers.** Start with basics — what T/S parameters are and why measured values beat datasheet values. Then step-by-step measurement instructions (REW impedance method) and a specific shopping list of everything to buy (measurement mic, USB interface/jig components, amp requirements, calipers, etc.). Owner has purchased nothing yet.
2. When tweeters arrive: measure dome opening diameter + recess depth (calipers) → finalize throat → generate test-fit ring STL, then full waveguide STL.

## Session log

- Session 6 (Aug 18, 2026): PE candidates evaluated (10 + Epique wildcard); RS225-8 CHOSEN. Enclosure redesigned to slim tower (11x11x39, 1.6 ft3 @ 28 Hz, L-fold slot port). README + CLAUDE fully updated. NEXT: measurement school + gear list (STILL pending), test-fit ring print, order woofers.

- Session 1 (Aug 3, 2026): Chose drivers, confirmed 2.5-way feasibility, picked TW030WA05 variant, designed enclosure + slot port (imperial), decided passive crossover, decided waveguide approach (front-mount OS over 115 mm faceplate, X1C one-piece print).
- Session 2 (Aug 4, 2026): Owner explored what-ifs; FINAL cab revised to 11 x 14 x 39" with 9.5 x 1-1/2" slot, 11-3/4" shelf (Fb ~33.5 Hz, F3 ~59). Driver centers shifted down 3" (tweeter 34-1/4" from cab bottom); use 1.5-2" plinth or slight back-tilt for ear height. Docs updated.
- Session 3 (Aug 5, 2026): Waveguide theory taught (beaming, directivity matching, loading gain, OS math). Corrected nominal geometry (45°→65° asymptote; mouth size dominates coverage at crossover). Wrote cad/waveguide_gen.py; generated waveguide.stl, testfit_ring.stl, profile.png. Measurement school still pending (owner deferred).
- Session 4 (Aug 9, 2026): Owner proposed Tritonia-style (at-horns.eu) rounded-rect mouth; taught diffraction-spreading rationale. Generator upgraded to v2: superellipse morph (throat circular, mouth 8 x 6.75" n=3.7, part 9 x 7.75 x 1.74", corner screws +/-3.14"). STLs regenerated. Round version = se_n 2. Mounting decided: front corner screws (#8 x 2.5", countersunk, +/-3.14" template; Bambu negative parts ok), foam gasket back face + pocket floor. Measurement school STILL pending.

## Reference links

- Woofer: https://www.parts-express.com/Dayton-Audio-RS225-8-8-Reference-Woofer-4-Ohm-295-378 (RS225-8, PN 295-378)
- Woofer data: Dayton publishes spec PDF + FRD/ZMA files on the PE product page
- Tweeter specs: http://www.wavecor.com/html/tw030wa05_to_08.html (use WA05 column)
- Tweeter source: https://www.cinergyaudio.com/products/wavecor-tw030wa05-30mm-textile-dome-tweeter-4-ohm-buyout
- Tweeter full spec PDF w/ outline dims (115 OD / 105 BC / 4 thick / 43 deep, mm): https://www.wavecor.com/Driver%20specifications%20PDF/TW030WA05_06_07_08_specifications.pdf

## Tooling assumptions

- Box sim: Python (T/S model) or VituixCAD/WinISD on owner's machine
- Waveguide: cad/waveguide_gen.py v2 DONE (numpy-stl; edit params at top, rerun). Superellipse-morphed OS (Tritonia-inspired): throat 1.5" nominal PENDING calipers; 65° asymptote; mouth 8 x 6.75" n=3.7; part 9 x 7.75 x 1.74". se_n=2 recovers round. Print testfit_ring.stl before full part.
- Measurement: REW + calibrated mic (confirm owner has one)

## Conventions

- Decisions log lives in README.md; this file holds working context only
- When generating geometry/code, save under /sim, /cad, /crossover subfolders## WOOFER DECISION (Aug 18, 2026): Dayton RS225-8 — CLOSED

18 candidates surveyed (5 Madisound/Cinergy + 10 Parts Express + Epique wildcard + Multicomp + Wavecor). Winner: RS225-8 on price/performance: F3 43 Hz in 1.6 ft³ slim tower, fully documented through the 1.7-1.9 kHz crossover region, ~$270/four. Runners-up: Satori MW19P-8 (quality, $760), Epique E180HE-44 (35 Hz F3 in 1.2 ft³ but subwoofer motor + 83.7 dB, $560). Multicomp dropped (800-900 Hz ceiling per experienced users, incompatible with tweeter's ~1.4-1.5 kHz passive floor). Full survey data in session history; sims reproducible via sim/box_sim.py. Enclosure redesigned: slim tower 11 x 11 x 39, 1.6 ft3 @ 28 Hz, 9.5 x 1" slot port w/ L-fold ~17". README updated. Amp headroom (Buckeye NCx252MP) makes 86.8 dB sensitivity a non-issue.

## Reference links

- Woofer: https://www.parts-express.com/Dayton-Audio-RS225-8-8-Reference-Woofer-4-Ohm-295-378 (RS225-8, PN 295-378)
- Woofer data: Dayton publishes spec PDF + FRD/ZMA files on the PE product page
- Tweeter specs: http://www.wavecor.com/html/tw030wa05_to_08.html (use WA05 column)
- Tweeter source: https://www.cinergyaudio.com/products/wavecor-tw030wa05-30mm-textile-dome-tweeter-4-ohm-buyout
- Tweeter full spec PDF w/ outline dims (115 OD / 105 BC / 4 thick / 43 deep, mm): https://www.wavecor.com/Driver%20specifications%20PDF/TW030WA05_06_07_08_specifications.pdf

## Tooling assumptions

- Box sim: Python (T/S model) or VituixCAD/WinISD on owner's machine
- Waveguide: cad/waveguide_gen.py v2 DONE (numpy-stl; edit params at top, rerun). Superellipse-morphed OS (Tritonia-inspired): throat 1.5" nominal PENDING calipers; 65° asymptote; mouth 8 x 6.75" n=3.7; part 9 x 7.75 x 1.74". se_n=2 recovers round. Print testfit_ring.stl before full part.
- Measurement: REW + calibrated mic (confirm owner has one)

## Conventions

- Decisions log lives in README.md; this file holds working context only
- When generating geometry/code, save under /sim, /cad, /crossover subfolders
