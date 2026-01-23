"""Weather Station Dashboard - Main Entry Point"""

import sys
import time

from src import utils
from src.config import config
from src.thresholds import ThresholdChecker
from src import pipeline

def display_reading(result):
    """Display a formatted reading."""
    print("\n" + "=" * 60)
    print(f"  READING - {result['timestamp_formatted']}")
    print("=" * 60)
    
    reading = result['reading']
    temp_f = utils.celsius_to_fahrenheit(reading['temperature'])
    print(f"  Temperature: {reading['temperature']}°C ({temp_f:.1f}°F)")
    print(f"  Humidity:    {reading['humidity']}%")
    
    if result['is_valid']:
        print(f"  Status:      ✓ Valid")
    else:
        print(f"  Status:      ✗ {result['error']}")
    
    if result['alerts']:
        print(f"\n  ⚠️  ALERTS ({len(result['alerts'])}):")
        for alert in result['alerts']:
            print(f"    - {alert['message']}")
    else:
        print(f"\n  ✓ All readings normal")
    print("=" * 60)

def main():
    """Main application entry point."""
    print("\n🌡️  Weather Station Starting...")
    config.display()
    
    checker = ThresholdChecker(
        config.temp_min, config.temp_max,
        config.humidity_min, config.humidity_max
    )
    
    print("\n📊 Monitoring (Press Ctrl+C to stop)...\n")
    
    try:
        cycle = 1
        while True:
            print(f"\n--- Cycle {cycle} ---")
            reading = pipeline.generate_mock_reading()
            result = pipeline.process_reading(reading, checker, utils)
            display_reading(result)
            
            print(f"\n⏳ Next reading in {config.read_interval}s...")
            time.sleep(config.read_interval)
            cycle += 1
            
    except KeyboardInterrupt:
        print("\n\n🛑 Stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()