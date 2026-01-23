"""Utility functions for weather station."""

from datetime import datetime

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def format_timestamp(dt=None):
    """Format datetime as ISO 8601 string."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def validate_temperature(temp):
    """Validate temperature is within sensor range."""
    if not -40 <= temp <= 80:
        raise ValueError(f"Temperature {temp} out of range")
    return True

def validate_humidity(humidity):
    """Validate humidity is 0-100%."""
    if not 0 <= humidity <= 100:
        raise ValueError(f"Humidity {humidity} must be 0-100")
    return True

if __name__ == "__main__":
    print("Testing utils...")
    print(f"25°C = {celsius_to_fahrenheit(25)}°F")
    print(f"Time: {format_timestamp()}")
