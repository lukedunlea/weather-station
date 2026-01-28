import time
import math
from datetime import datetime
from ADCDevice import *  # Imports the ADC code from the other file

# Create a basic ADC object
adc = ADCDevice()

# Set temperature limits for warnings (in °C)
TEMP_MIN = 5
TEMP_MAX = 30

def setup():
    global adc

    # Check which ADC chip is connected
    if adc.detectI2C(0x48):          # PCF8591 address
        adc = PCF8591()
        print("PCF8591 detected")

    elif adc.detectI2C(0x4b):        # ADS7830 address
        adc = ADS7830()
        print("ADS7830 detected")

    else:
        # If no ADC is found, stop the program
        print(
            "No correct I2C address found.\n"
            "Please run: i2cdetect -y 1\n"
            "Program Exit."
        )
        exit(1)


def loop():
    while True:
        # Read the analogue value from channel A0
        value = adc.analogRead(0)

        # Convert the ADC value into a voltage (0–3.3V)
        voltage = value / 255.0 * 3.3

        # Work out the thermistor resistance
        Rt = 10 * voltage / (3.3 - voltage)

        # Convert resistance into temperature using a formula
        tempK = 1 / (1 / (273.15 + 25) + math.log(Rt / 10) / 3950.0)
        tempC = tempK - 273.15

        # Get the current time for the reading
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Print the readings to the terminal
        print(
            f"[{timestamp}] "
            f"ADC: {value:3d} | "
            f"Voltage: {voltage:.2f} V | "
            f"Temperature: {tempC:.2f} °C",
            end=""
        )

        # Display a warning if the temperature is outside the safe range
        if tempC < TEMP_MIN:
            print("  ⚠️  Warning: Temperature is too low")

        elif tempC > TEMP_MAX:
            print("  ⚠️  Warning: Temperature is too high")

        else:
            print()

        # Wait 1 second before reading again
        time.sleep(1)


def destroy():
    # Close the ADC properly when stopping the program
    adc.close()


if __name__ == '__main__':
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")



