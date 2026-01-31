from time import sleep, time
from gpiozero import LED
import smbus

try:
    print('Ready')

    # I2C configuration
    i2c_address = 0x68  # Default I2C address (change as needed)
    i2c_bus = smbus.SMBus(1)  # Bus 1 for Raspberry Pi Zero
    
    # Pin number can be BCM or physical
    # gpiozero uses BCM by default
    led1 = LED(5)

    led1.off()
    
    last_send_time = time()

    while True:
        current_time = time()
        
        # Send "alive!" every 10 seconds
        if current_time - last_send_time >= 10:
            try:
                message = "alive!"
                # Send as byte string
                i2c_bus.write_i2c_block_data(i2c_address, 0, [ord(c) for c in message])
                print(f"Sent: {message}")
                last_send_time = current_time
            except Exception as e:
                print(f"Error sending I2C message: {e}")
        
        # Try to receive incoming data
        try:
            data = i2c_bus.read_i2c_block_data(i2c_address, 0, 32)
            if data:
                message = ''.join([chr(b) for b in data if b != 0])
                if message:
                    print(f"Received: {message}")
        except Exception as e:
            pass  # Silently ignore read errors when no data available
        
        # LED blink pattern
        for i in range(1, 32):
            if i % 2 == 0:
                led1.on()
            else:
                led1.off()
            sleep(0.1)

        led1.off()
        sleep(1)

except KeyboardInterrupt:
    print ("Exiting on user abort\n")

except Exception as e:
    print ("General error occurred\n")
    print (e)
