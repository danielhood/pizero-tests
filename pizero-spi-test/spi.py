import spidev
import time

# Function to initialize SPI
def init_spi():
    spi = spidev.SpiDev()
    spi.open(0, 0)  # Open SPI port 0, device (CS) 0
    spi.max_speed_hz = 1000000  # Set max speed to 1 MHz
    return spi

# Function to write data to the SPI bus
def write_spi(spi, data):
    print(f"Writing data: {data}")
    bytes_written = spi.writebytes(data)
    print(f"Wrote {bytes_written} bytes")

# Function to read data from the SPI bus
def read_spi(spi, length=8):
    print("Reading data...")
    data_read = spi.readbytes(length)
    print(f"Read data: {data_read}")
    return data_read

if __name__ == "__main__":
    try:
        # Initialize SPI
        spi = init_spi()

        while True:
            # Write "test" string to the SPI bus
            write_spi(spi, b'test')

            # Pause for 10 seconds
            time.sleep(10)

            # Read 8 bytes from the SPI bus
            read_data = read_spi(spi)

    except KeyboardInterrupt:
        print("Exiting on user abort")

    finally:
        # Close the SPI connection
        spi.close()
