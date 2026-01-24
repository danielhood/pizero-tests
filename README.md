# pizero-light-test

A small example project that demonstrates controlling LEDs on a Raspberry Pi Zero (or compatible Pi) using `gpiozero`.

**Files**
- `pizero-light-test/lights.py`  main script that blinks four LEDs in a simple pattern.

**Overview**
This repository contains a minimal script to exercise GPIO outputs on a Raspberry Pi. It's useful for hardware testing or learning how to use `gpiozero` with physical LEDs.

**Requirements**
- Python 3.8+ (3.11 recommended)
- On Raspberry Pi hardware: `gpiozero` (which will use an appropriate pin backend such as `RPi.GPIO` or `pigpio`).

**Setup**
1. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate  # Linux / macOS
```

2. Install the dependency (on the Pi):

```bash
pip install gpiozero
```

**Wiring**
- The script uses BCM GPIO pin numbers: 5, 7, 9, and 15 (as configured in `lights.py`).
- Confirm whether you are using BCM or physical (BOARD) numbering when wiring; `gpiozero` uses BCM by default.

**Usage**
- Run the script on a Raspberry Pi:

```bash
python pizero-light-test/lights.py
```

- Or, from the repository root using the explicit path:

```bash
python pizero-light-test/lights.py
```

- Stop with `Ctrl+C`.

**Notes**
- On non-Raspberry Pi systems, importing `gpiozero` may fail or not control real hardware. For development or CI, consider using `gpiozero`'s mock pin factory (`GPIOZERO_PIN_FACTORY=mock`) or run the script on a Pi.

**Contributing**
- Pull requests and issues welcome. Keep changes focused and add short usage notes for hardware changes.

**License**
- MIT
