"""Data processing pipeline for weather station."""

from datetime import datetime
import logging
import random
from src.logger import setup_logger
import src.utils as utils_module

logger = setup_logger(__name__)

def generate_mock_reading():
    """Generate simulated sensor data.
    
    Returns:
        Dict with temperature, humidity, timestamp
    """

    mockReading = {
        "temperature": round(random.uniform(-100, 200), 1),
        "humidity": round(random.uniform(-100, 200), 1),
        "timestamp": datetime.now(),
        "message": "these are your mock readings"

    }

    logger.info(f"The mock reading is : {mockReading} ")

    return mockReading

def process_reading(mockReading):
    """Process a sensor reading through the pipeline.
    
    Returns:
        Dict with processed data and alerts
    """

    temp = mockReading["temperature"]
    humidity = mockReading["humidity"]
    timestamp = mockReading["timestamp"]
    
    # Validate
    isTempValid = utils_module.validate_temperature(temp)
    isHumValid = utils_module.validate_humidity(humidity)
    if isTempValid and isHumValid:
        is_valid = True
        logger.info(f"The temp is inside the given threshold: {temp}")
    else:
        is_valid = False
        logger.warning(f"The temp is outside the given threshold: {temp}")
        logger.error(f"Your humidity has gone outside the given threshold{humidity}")
        print("test")
    
    
    return {
        "reading": mockReading,
        "is_valid": is_valid,
        "timestamp_formatted": utils_module.format_timestamp(timestamp)
    }

def testRun():

    for i in range (1,20):
        print("Testing pipeline...")
        mockReading = generate_mock_reading()
        print(f"Mock: {mockReading['temperature']}°C, {mockReading['humidity']}%, {mockReading["message"]}")
        pr = process_reading(mockReading)
        print(f"{pr}")

if __name__ == "__main__":

    for i in range (1,20):
        print("Testing pipeline...")
        mockReading = generate_mock_reading()
        print(f"Mock: {mockReading['temperature']}°C, {mockReading['humidity']}%, {mockReading["message"]}")
        pr = process_reading(mockReading)
        print(f"{pr}")
