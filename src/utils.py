"""Utility functions for weather station."""

from datetime import datetime
import logging
import random
from logger import setup_logger

logger = setup_logger("myApp", "utilsLog.log", logging.DEBUG)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    logger.info(f"The current temp in celsius is: {celsius} and the converted temp to fahrenheit is: {fahrenheit}")
 
    return fahrenheit

def format_timestamp(dt=None):
    """Format datetime as ISO 8601 string."""
    
    if dt is None:
        dt = datetime.now()
        logger.info(f"the current time is: {dt}")
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def validate_temperature(temp):
    """Validate temperature is within sensor range."""
    logger.info(f"the temp is {temp}")
    
    if not -40 <= temp <= 80:
        logger.warning(f"The temperature is: {temp} this is out of range.")
        # raise ValueError(f"Temperature {temp} out of range")
    return True

def validate_humidity(humidity):
    """Validate humidity is 0-100%."""
    logger.info(f"the humidity is {humidity}")
 
    if not 0 <= humidity <= 100:
        logger.error(f"The humidity is: {humidity} this is out of range.")
        # raise ValueError(f"Humidity {humidity} must be 0-100")
    return True

if __name__ == "__main__":

   

    for i in range (1,20):
        hum = random.randint(-5,105)
        temp = random.randint(-50,100)
            
        print("Testing utils...")
        print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
        print(f"Time: {format_timestamp()}")
        print(f"{validate_temperature(temp)}")
        print(f"{validate_humidity(hum)}")