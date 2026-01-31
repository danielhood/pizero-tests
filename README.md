# pizero-tests

Test suite for Raspberry Pi Zero GPIO and I2C functionality.

##Files
- `pizero-light-test/lights.py` - Main script that blinks 5 LEDs in a repeating pattern using `gpiozero`.
- `pizero-i2c-test/i2c.py` - I2C send/receive test script that sends "alive!" every 10 seconds and prints any incoming messages.

## Quickstart
Requirements:
- Python 3.8+ (3.11 recommended)
- On Raspberry Pi: `gpiozero` and `smbus-cffi` for I2C support.

### Setup:

#### /boot/firmware/config.txt
##### I2C:
To load i2c_bcm2835, uncomment (or add if not present) the following line in config.txt to enable the primary I2C interface on GPIO pins 2 (SDA) and 3 (SCL):

```
dtparam=i2c_arm=on
```

(Optional) Adjust I2C Speed: The default I2C baudrate is 100,000 Hz which is usually fine for most applications. If needed (e.g., for faster communication up to 400,000 Hz), you can add another line to specify a new baudrate:

```
dtparam=i2c_arm_baudrate=400000
```

Once config.txt is updated to load the i2c module, and the pizero is rebooted, enable i2c through `sudo raspi-config` under **3 Interfacing Options > I5 I2C**.

 Verify that I2C is enabled by checking the following (all need to return things): 

```lsmod | grep i2c
ls /dev/i2c*
i2cdetect -l
```
##### PWM Audio:

```
dtoverlay=audremap,pins_12_13
```
Enable audio (loads snd_bcm2835)
```
dtparam=audio=on
```

Increase the audio level using `alsamixer`.

Test aduio with (note this will test both channels, but h/w may only be setup for one channel):
```
speaker-test -t sine -f 440 -c 2
```

#### Packages
```bash
sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install python3-gpiozero python3-smbus
```
Note: For this project we are installing modules through apt-get globally instead of pip (and also not using venv).

**LED Test**
Run (from repo root):
```bash
python pizero-light-test/lights.py
```
Blinks 5 LEDs in a repeating pattern. Stop with `Ctrl+C`.

**I2C Test**
Run (from repo root):
```bash
python pizero-i2c-test/i2c.py
```
Sends "alive!" every 10 seconds on I2C channel and prints any incoming strings to the console. The default I2C address is `0x68` (configurable in the script). Stop with `Ctrl+C`.

**Pin mapping (BCM numbers)**
- LED 1: BCM 5
- LED 2: BCM 7
- LED 3: BCM 9
- LED 4: BCM 11
- LED 5: BCM 15  (note: BCM 12 & 13 / physical pins 32 & 33 are reserved for PCM audio for our test config)

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

License:
- MIT
