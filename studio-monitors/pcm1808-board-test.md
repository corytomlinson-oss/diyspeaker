# PCM1808 Board Test: Static and Functional

Purpose: check whether the PCM1808 module has the low-pass input filter described in the seller's listing (10 kΩ resistor and 0.1 µF capacitor, cutoff about 159 Hz). If it does, the board needs rework before use. If it doesn't, the board can go into the build.

This guide is written for a beginner. Read the whole guide before you start. If anything is unclear, stop and ask rather than guessing.

---

## Part 0: Safety and setup

### Rules to follow every time

1. **Power off before touching the board.** Unplug the USB cable or switch off the bench supply before you change any wires or probe the board.
2. **Use only low voltage.** This test uses 5 V or less from USB or a bench supply. Never work on mains power in this test.
3. **Touch the board by its edges.** Static electricity can damage the chip. If you can, touch a grounded metal object first, or use a wrist strap.
4. **Don't bridge pins by accident.** Pins are very close together. After soldering or probing, look again before powering on.
5. **Check polarity on electrolytic capacitors.** They have a marked side and a stripe on the can. Reverse polarity can break them.

### Tools

| Item | Purpose | Notes |
|---|---|---|
| Digital multimeter (DMM) | Measure resistance and voltage | Any basic DMM works. Needs a resistance (Ω) setting and a voltage (V) setting. |
| PCM1808 module | Device under test | The module you bought. |
| Raspberry Pi Pico 2 | Reads the digital output | Needs a USB cable and a computer to load code. |
| Jumper wires (female-to-female) | Connect module to Pico | About 6 wires. |
| Signal generator (or a phone tone app as a rough alternative) | Creates a test tone | A dedicated generator is more accurate. |
| Audio cable with a 3.5 mm plug or alligator clips | Connects the generator to the board input | Match the generator output to the input. |
| Magnifying glass or phone camera | Read small silkscreen labels | Helpful for small markings. |

### Get to know the board

Look at the module and find these labels on the silkscreen (the white printed text on the board). Write them down.

- **RIN** and **LIN**: the right and left analog inputs. These are the pads where the signal goes in.
- **GND**: ground. This is the common return for the whole circuit.
- **3.3** and **+5V**: power pins. The 5 V pin is the input. The 3.3 V pin is an output from the board's regulator. Don't power the board from 3.3 V.
- **BCK, OUT, LRC, SCK**: the digital pins. BCK is the bit clock, OUT is the data, LRC is the left/right clock, and SCK is the system clock.
- **FMY, MD1, MDO**: mode pins. These set how the chip works. Check the silkscreen to see which pins are tied high or low on your board before you power it.

Take a clear photo of the whole board with the labels visible. Keep it with the test log.

---

## Part 1: Static test (power OFF)

Goal: check resistance on the input path without powering the board.

### Step 1: Prepare the multimeter

1. Turn the meter on.
2. Set the dial to the resistance setting (Ω). Use the lowest range that covers 10 kΩ, often labeled 20 kΩ or 200 kΩ.
3. Plug the black probe into the **COM** jack and the red probe into the **VΩ** jack.
4. Touch the two probe tips together. The reading should be close to 0 Ω. Note the reading. This is your probe resistance (usually under 1 Ω).

### Step 2: Confirm the board is unpowered

1. Unplug the USB cable and any other power.
2. Wait at least 1 minute so any stored charge drains.

### Step 3: Find the input components

1. Locate the RIN pad (the right input) on the silkscreen.
2. Find the nearest small resistor and small capacitor connected to that pad. Resistors are usually small rectangles with two metal ends. Capacitors are usually small rectangles with two metal ends. Electrolytic capacitors are round cans, which are not the part we're checking here.
3. Look at the top marking on the resistor. Some resistors are marked with a code such as `103`. This means 10 × 10³ = 10 kΩ.
4. Look at the top marking on the capacitor. Ceramic capacitors are often marked `104`. This means 10 × 10⁴ pF = 100,000 pF = 0.1 µF.

Write down what you see for each part. If the marking isn't clear, don't guess. Note it as "unclear."

### Step 4: Measure resistance from the input to ground

1. Put the black probe on **GND**.
2. Put the red probe on the **RIN** pad.
3. Read the meter.

Interpret the reading:

| Reading | Meaning |
|---|---|
| About 10 kΩ | The 10 kΩ resistor is probably connected from RIN to ground. This matches the seller's claim. |
| Much lower than 10 kΩ (for example, a few hundred ohms) | Something else is loading the input. Check for solder bridges or other connections. |
| Open, or "OL" (overload) on the meter | There is no path from RIN to ground. The 10 kΩ resistor may be in a different place or missing. |

A reading of about 10 kΩ doesn't prove the filter is there, because the capacitor blocks DC. It only shows that the resistor path is present.

### Step 5: Check the capacitor (optional)

Most basic multimeters can't measure a 0.1 µF capacitor reliably. If your meter has a capacitance setting (labeled with F), you can try:

1. Set the meter to capacitance (F).
2. Remove the module from any connections.
3. Measure across the capacitor's two pads.
4. Compare the reading to 0.1 µF (100 nF).

If your meter has no capacitance setting, skip this step and note "not measured." An LCR meter gives a better reading.

### Step 6: Record the static test

Write the results in the test log (Part 3).

---

## Part 2: Functional test (power ON)

Goal: send a known tone through the input and measure how the output level changes with frequency. A board with the 159 Hz filter will lose a lot of level as frequency rises.

### What you expect to see

For a single-pole low-pass at 159 Hz:

| Frequency | Expected level relative to 1 kHz |
|---|---|
| 100 Hz | About +14 dB (higher than 1 kHz, but about −1.4 dB from a flat response) |
| 1 kHz | Reference (about −16 dB below a flat response) |
| 10 kHz | About −20 dB relative to 1 kHz |

Put simply: if the board has the filter, the level at 1 kHz and 10 kHz will be far apart, roughly 20 dB. A board without the filter will show 1 kHz and 10 kHz within about 1 dB of each other.

### Step 1: Set up the Pico as a receiver

The Pico reads the digital output from the module. Writing and loading that program is a separate step, which we'll do together. Don't power the module until the receiver program is ready and the wiring is checked.

### Step 2: Wire the module to the Pico

Power off everything first.

| Module pin | Pico connection | Purpose |
|---|---|---|
| +5V | Pico 5V output (VBUS, if powering from USB) | Power in |
| GND | Pico GND | Common ground |
| BCK | Pico GPIO pin assigned in the receiver program | Bit clock |
| LRC | Pico GPIO pin assigned in the receiver program | Left/right clock |
| OUT | Pico GPIO pin assigned in the receiver program | Data |

Use the pin numbers from the receiver program. Don't use any pin number from memory. Check the module's SCK and mode pins against the silkscreen and the module's notes. If you don't know how to set them, ask before powering on.

### Step 3: Wire the signal generator to the input

1. Turn the signal generator off.
2. Connect the generator's **ground** (or shield) to the module's **GND** pin.
3. Connect the generator's **signal** wire to the module's **RIN** pad.
4. Set the generator to a low output level, such as 0.5 V RMS (about 1.4 V peak-to-peak). Keep the level under 1 V RMS. The input is designed for about 3 V peak-to-peak full scale, and starting low protects the chip.

Note: If your generator has a 50 Ω output and the input has a high impedance, the level you see may differ from what you set. Check the level with the multimeter's AC voltage setting if you can.

### Step 4: Power up and check the basics

1. Connect the Pico's USB cable to the computer. This powers the Pico and the module.
2. Turn on the generator, set it to **100 Hz**, and check the Pico's output. You should see data.
3. If you see no data, or all zeros, stop. Check the wiring and power, then ask for help.

### Step 5: Measure each frequency

Measure at three frequencies with the same generator level: **100 Hz**, **1 kHz**, and **10 kHz**.

For each frequency:

1. Set the generator to the frequency.
2. Let the output settle for a few seconds.
3. Record the level the receiver program reports.
4. Keep the generator level the same for all three frequencies. Only change the frequency.

### Step 6: Interpret the result

Compare 1 kHz and 10 kHz:

| Result | Meaning |
|---|---|
| 1 kHz and 10 kHz within about 1 dB of each other | No strong low-pass filter at 159 Hz. The board passes the test. |
| 1 kHz is about 16 dB lower than 100 Hz, and 10 kHz is about 20 dB lower than 1 kHz | Matches the 159 Hz filter. The board needs rework. |
| Other large differences | Record the numbers and ask for help. The cause may be wiring, level, or the generator. |

Repeat the test on the second channel (LIN) if you can, and note whether the two channels match.

---

## Part 3: Test log

Copy this table into your notes or into the repo, and fill it in for each board.

| Date | Board ID | Test | Result | Notes |
|---|---|---|---|---|
| | | Static: RIN to GND resistance | | |
| | | Static: resistor marking (RIN) | | |
| | | Static: capacitor marking (RIN) | | |
| | | Functional: 100 Hz level | | |
| | | Functional: 1 kHz level | | |
| | | Functional: 10 kHz level | | |
| | | Functional: LIN channel | | |
| | | Pass or fail | | |

---

## Part 4: If the board fails

1. Power off and wait 1 minute.
2. Take clear photos of the input area.
3. Don't rework the board yet. Confirm the test results and the component values first.
4. If the test confirms the filter, see the rework options in the README (Option A: 1 kΩ and 3.3 nF, or Option B: jumper the resistor and remove the shunt capacitor).
5. Never remove the series coupling capacitor. It's needed for correct DC bias.

---

## Notes and limits

- These tests check the input filter only. They don't prove that the rest of the board works.
- A basic multimeter may not measure the capacitor. Its results are approximate.
- The expected levels assume a simple single-pole filter. Real boards can differ, so compare results, not exact numbers.
- If anything is unclear or unexpected, stop and ask for help. Don't keep testing with an unclear setup.
