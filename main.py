"""Weather Station Dashboard - Main Entry Point"""
import sys
import time
from src import utils
from src.config import config
from src.thresholds import ThresholdChecker
from src import pipeline
from src.logger import setup_logger
import logging

# Set up main logger
logger = setup_logger(__name__, level= logging.DEBUG if config.debug_mode else logging.INFO)
def display_reading(result):
    """Display a formatted reading."""
    print("\n" + "=" * 60)
    print(f" READING - {result['timestamp_formatted']}")
    print("=" * 60)
    reading = result['reading']
    temp_f = utils.celsius_to_fahrenheit(reading['temperature'])
    print(f"  Temperature: {reading['temperature']}°C ({temp_f:.1f}°F)")
    print(f"  Humidity:    {reading['humidity']}%")

    if result['is_valid']:
        print(f"  Status:      ✓ Valid")
    else:
        print("error")

    # if result['alerts']:
        # print(f"⚠️alerts")
        
    # else:
    #     print(f"\n  ✓ All readings normal")
    print("=" * 60)

def main():
#Main application entry point."""
    logger.info("Weather Station Dashboard starting...")
config.display()

checker = ThresholdChecker(
    config.temp_min, config.temp_max,
    config.humidity_min, config.humidity_max
)
logger.info("Threshold checker initialized")

print("\n📊 Monitoring (Press Ctrl+C to stop)...\n")

try:
    cycle = 1
    while True:
        logger.info(f"Starting cycle {cycle}")
        
        reading = pipeline.generate_mock_reading()
        result = pipeline.process_reading(reading)
        display_reading(result)
        
        logger.info(f"Cycle {cycle} complete. Waiting {config.read_interval}s...")
        time.sleep(config.read_interval)
        cycle += 1
        
except KeyboardInterrupt:
    logger.info("Shutdown requested by user")
    print("\n\n🛑 Stopped by user")
    sys.exit(0)
except Exception as e:
    logger.critical(f"Unexpected error: {e}", exc_info=True)
    print(f"\n\n❌ ERROR: {e}")
    sys.exit(1)

if name == "main":
    main()
