"""
Sensor module for reading temperature and humidity
"""

def read_temperature():
    """
    Read temperature from DHT sensor
    Returns temperature in Celsius
    """
    # TODO: Implement sensor reading
    pass

def read_humidity():
    """
    Read humidity from DHT sensor
    Returns humidity percentage
    """
    # TODO: Implement sensor reading
    pass

def read_sensor_data():
    """
    Read both temperature and humidity
    Returns dictionary with both values
    """
    return {
        'temperature': read_temperature(),
        'humidity': read_humidity()
    }
