import smbus  # Allows the Raspberry Pi to communicate using I2C

class ADCDevice(object):
    def __init__(self):
        self.cmd = 0          # Command used by the ADC
        self.address = 0      # I2C address of the device
        self.bus = smbus.SMBus(1)  # Opens I2C bus 1 on the Pi

    def detectI2C(self, addr):
        # Checks if a device exists at this I2C address
        try:
            self.bus.write_byte(addr, 0)
            return True
        except:
            return False

    def close(self):
        # Closes the I2C connection
        self.bus.close()


class PCF8591(ADCDevice):
    def __init__(self):
        super(PCF8591, self).__init__()
        self.cmd = 0x40      # Default command
        self.address = 0x48  # Default I2C address

    def analogRead(self, chn):
        # Reads a value from one of the 4 analogue inputs
        value = self.bus.read_byte_data(self.address, self.cmd + chn)
        value = self.bus.read_byte_data(self.address, self.cmd + chn)
        return value

    def analogWrite(self, value):
        # Sends a value out through the analogue output
        self.bus.write_byte_data(self.address, self.cmd, value)


class ADS7830(ADCDevice):
    def __init__(self):
        super(ADS7830, self).__init__()
        self.cmd = 0x84
        self.address = 0x4b  # Default I2C address

    def analogRead(self, chn):
        # Reads a value from one of the 8 analogue inputs
        command = self.cmd | (((chn << 2 | chn >> 1) & 0x07) << 4)
        value = self.bus.read_byte_data(self.address, command)
        return value

