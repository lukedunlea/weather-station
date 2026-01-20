"""
Configuration settings for Weather Station Dashboard
"""
# GPIO Pin Configuration
LED_PIN_RED = 17
LED_PIN_GREEN = 27
LED_PIN_BLUE = 22
BUZZER_PIN = 23
# Sensor Configuration
DHT_SENSOR_PIN = 4
SENSOR_READ_INTERVAL = 5  # seconds
# Alert Thresholds
TEMP_HIGH_THRESHOLD = 28.0  # Celsius
TEMP_LOW_THRESHOLD = 15.0   # Celsius
HUMIDITY_HIGH_THRESHOLD = 70.0  # Percentage
HUMIDITY_LOW_THRESHOLD = 30.0   # Percentage
# Flask Configuration
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
DEBUG_MODE = True
