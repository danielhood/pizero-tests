import smbus


class I2CUtils:
    def __init__(self, i2c_address):
        self.i2c_bus = smbus.SMBus(1)  # Bus 1 for Raspberry Pi Zero
        self.i2c_address = i2c_address

    def send_data(self, data):
        try:
            # Send the text "test" to the I2C device
            self.i2c_bus.write_i2c_block_data(self.i2c_address, 0, list(data))
            print("Sent: 'test'")
        except smbus.SMBusError as e:
            print(f"I2C write error: {e}")
        except Exception as e:
            print(f"General error occurred during I2C write: {e}")

    def receive_data(self):
        try:
            # Try to receive incoming data
            print('Attempting read...')
            data = self.i2c_bus.read_i2c_block_data(self.i2c_address, 0, 16)  # Changed from 32 to 16
            if data:
                message = ''.join([chr(b) for b in data if b != 0])
                if message:
                    return message
        except smbus.SMBusError as e:
            print(f"I2C read error: {e}")
        except Exception as e:
            print(f"General error occurred during I2C read: {e}")
        return None
