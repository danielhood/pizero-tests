# pizero-light-test

A minimal example that blinks five LEDs on a Raspberry Pi Zero (or compatible Pi) using `gpiozero`.

**Files**
- `pizero-light-test/lights.py`  main script that blinks 5 LEDs in a repeating pattern.

**Quickstart**
Requirements:
- Python 3.8+ (3.11 recommended)
- On Raspberry Pi: `gpiozero` (it will select a suitable backend such as `RPi.GPIO` or `pigpio`).

Setup:
```bash
python -m venv .venv
.venv\Scripts\activate    # Windows (PowerShell/Cmd)
source .venv/bin/activate  # Linux / macOS
pip install gpiozero
```

Run (from repo root):
```bash
python pizero-light-test/lights.py
# or explicitly
python ./pizero-light-test/lights.py
```
Stop with `Ctrl+C`.

**Pin mapping (BCM numbers)**
- LED 1: BCM 5
- LED 2: BCM 7
- LED 3: BCM 9
- LED 4: BCM 11
- LED 5: BCM 15  (note: BCM 13 / physical pin 33 is reserved for PCM audio in some Pi models)

Notes:
- `gpiozero` uses BCM numbering by default. Verify wiring before powering your hardware.

Testing / development on non-Pi systems:
- To run without hardware, use `gpiozero`'s mock pin factory. Example (bash):

```bash
export GPIOZERO_PIN_FACTORY=mock
python pizero-light-test/lights.py
```

PowerShell example:
```powershell
$env:GPIOZERO_PIN_FACTORY = 'mock'
python pizero-light-test/lights.py
```

Troubleshooting:
- Import errors for `gpiozero` indicate the package is not installed in the active Python environment.
- If LEDs don't behave as expected, double-check pin numbering (BCM vs BOARD), wiring, and resistor placement.

Contributing:
- PRs and issues welcome. Keep hardware changes documented in the README.

License:
- MIT
