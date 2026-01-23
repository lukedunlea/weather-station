"""Alert threshold evaluation logic."""
class ThresholdChecker:
    """Evaluates sensor readings against thresholds."""
    
    def __init__(self, temp_min, temp_max, humidity_min, humidity_max):
        """Initialize thresholds."""
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.humidity_min = humidity_min
        self.humidity_max = humidity_max
    
    def check_temperature(self, temperature):
        """Check temperature. Returns alert dictionary or None."""
        if temperature < self.temp_min:
            return {
                "type": "LOW_TEMPERATURE",
                "value": temperature,
                "message": f"Temp {temperature}°C below min {self.temp_min}°C"
            }
        elif temperature > self.temp_max:
            return {
                "type": "HIGH_TEMPERATURE",
                "value": temperature,
                "message": f"Temp {temperature}°C above max {self.temp_max}°C"
            }
        return None
    
    def check_humidity(self, humidity):
        """Check humidity. Returns alert dict or None."""
        if humidity < self.humidity_min:
            return {
                "type": "LOW_HUMIDITY",
                "value": humidity,
                "message": f"Humidity {humidity}% below min {self.humidity_min}%"
            }
        elif humidity > self.humidity_max:
            return {
                "type": "HIGH_HUMIDITY",
                "value": humidity,
                "message": f"Humidity {humidity}% above max {self.humidity_max}%"
            }
        return None
    
    def check_all(self, temperature, humidity):
        """Check all readings. Returns list of alerts."""
        alerts = []
        temp_alert = self.check_temperature(temperature)
        if temp_alert:
            alerts.append(temp_alert)
        humidity_alert = self.check_humidity(humidity)
        if humidity_alert:
            alerts.append(humidity_alert)
        return alerts

if __name__ == "__main__":
    print("Testing thresholds...")
    checker = ThresholdChecker(15, 30, 30, 70)
    alerts = checker.check_all(35, 25)
    print(f"Alerts: {len(alerts)}")
    for alert in alerts:
        print(f"  {alert['message']}")
