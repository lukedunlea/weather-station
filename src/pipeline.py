"""Data processing pipeline for weather station."""

import random
from datetime import datetime

def generate_mock_reading():
    """Generate simulated sensor data.
    
    Returns:
        Dict with temperature, humidity, timestamp
    """
    return {
        "temperature": round(random.uniform(10, 35), 1),
        "humidity": round(random.uniform(20, 80), 1),
        "timestamp": datetime.now()
    }

def process_reading(reading, threshold_checker, utils_module):
    """Process a sensor reading through the pipeline.
    
    Returns:
        Dict with processed data and alerts
    """
    temp = reading["temperature"]
    humidity = reading["humidity"]
    timestamp = reading["timestamp"]
    
    # Validate
    try:
        utils_module.validate_temperature(temp)
        utils_module.validate_humidity(humidity)
        is_valid = True
        error = None
    except ValueError as e:
        is_valid = False
        error = str(e)
    
    # Check thresholds
    alerts = []
    if is_valid:
        alerts = threshold_checker.check_all(temp, humidity)
    
    return {
        "reading": reading,
        "is_valid": is_valid,
        "error": error,
        "alerts": alerts,
        "timestamp_formatted": utils_module.format_timestamp(timestamp)
    }

if __name__ == "__main__":
    print("Testing pipeline...")
    reading = generate_mock_reading()
    print(f"Mock: {reading['temperature']}°C, {reading['humidity']}%")