"""Configuration management for weather station."""

import os
from dotenv import load_dotenv
from src.logger import setup_logger

load_dotenv()
logger = setup_logger(__name__)


class Config:
    """Application configuration."""

    def __init__(self):
        """Initialize with defaults and env overrides."""
        self.sensor_model = os.getenv("SENSOR_MODEL", "DHT22")
        self.gpio_pin = int(os.getenv("GPIO_PIN", "4"))
        self.read_interval = int(os.getenv("READ_INTERVAL", "60"))

        self.temp_min = float(os.getenv("TEMP_MIN", "15.0"))
        self.temp_max = float(os.getenv("TEMP_MAX", "30.0"))
        self.humidity_min = float(os.getenv("HUMIDITY_MIN", "30.0"))
        self.humidity_max = float(os.getenv("HUMIDITY_MAX", "70.0"))

        self.debug_mode = os.getenv("DEBUG", "False").lower() == "true"

        logger.info("Configuration loaded")
        logger.debug(
            f"Temp={self.temp_min}-{self.temp_max}, "
            f"Humidity={self.humidity_min}-{self.humidity_max}, "
            f"Debug={self.debug_mode}"
        )

    def display(self):
        """Display current configuration."""
        print("=== Configuration ===")
        print(f"Sensor: {self.sensor_model} on GPIO {self.gpio_pin}")
        print(f"Temp Range: {self.temp_min}°C - {self.temp_max}°C")
        print(f"Humidity Range: {self.humidity_min}% - {self.humidity_max}%")
        print(f"Read Interval: {self.read_interval}s")
        print("=" * 21)


config = Config()

if __name__ == "__main__":
    config.display()

