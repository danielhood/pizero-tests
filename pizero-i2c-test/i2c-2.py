from i2c_utils import send_data, receive_data
from gpiozero import LED

def main():
    try:
        print('Ready')

        # Create an instance of I2CUtils
        i2c_utils = I2CUtils(i2c_address=0x60)

        # Define the byte array containing the text "test"
        test_data = b'test'

        print ('Creating leds...')
        # Pin number can be BCM or physical
        # gpiozero uses BCM by default
        led1 = LED(5)

        print ('Clearing led state...')
        led1.off()

        last_send_time = time()

        print('Starting main loop...')

        while True:
            current_time = time()

            # Send the text "test" to the I2C device
            if test_time - last_send_time > 1:  # Send every second
                i2c_utils.send_data(list(test_data))
                last_send_time = current_time

            # Receive incoming data and process it
            received_data = i2c_utils.receive_data()
            if received_data:
                print(f"Received Data: {received_data}")
    
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

if __name__ == "__main__":
    main()