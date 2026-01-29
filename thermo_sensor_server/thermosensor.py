import math
from datetime import datetime
from ADCDevice import *

class ThermoSensor:
    def __init__(self):
        # Create ADC object
        self.adc = ADCDevice()

        # Detect connected ADC
        if self.adc.detectI2C(0x48):
            self.adc = PCF8591()
            print("PCF8591 detected")
        elif self.adc.detectI2C(0x4b):
            self.adc = ADS7830()
            print("ADS7830 detected")
        else:
            raise RuntimeError(
                "No correct I2C address found. "
                "Please run: i2cdetect -y 1"
            )

    def read_temperature(self):
        # Read ADC value
        value = self.adc.analogRead(0)

        # Convert ADC value to voltage
        voltage = value / 255.0 * 3.3

        # Calculate thermistor resistance
        Rt = 10 * voltage / (3.3 - voltage)

        # Convert resistance to temperature (°C)
        tempK = 1 / (1 / (273.15 + 25) + math.log(Rt / 10) / 3950.0)
        tempC = tempK - 273.15

        return {
            "temperature": round(tempC, 2),
            "voltage": round(voltage, 2),
            "adc": value,
            "time": datetime.now().strftime("%H:%M:%S")
        }

    def close(self):
        self.adc.close()



