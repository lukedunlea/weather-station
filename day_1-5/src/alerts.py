"""
Alert system for Weather Station.
"""
class AlertManager:
    """Checks sensor values against thresholds and triggers alerts."""
    def __init__(self, high_temp, low_temp, high_humidity, low_humidity):
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.high_humidity = high_humidity
        self.low_humidity = low_humidity
    def evaluate(self, temperature, humidity):
        """
        Evaluate the current readings and return a list of active alerts.
        """
        alerts = []
        if temperature > self.high_temp:
            alerts.append("HIGH_TEMPERATURE")
        if temperature < self.low_temp:
            alerts.append("LOW_TEMPERATURE")
        if humidity > self.high_humidity:
            alerts.append("HIGH_HUMIDITY")
        if humidity < self.low_humidity:
            alerts.append("LOW_HUMIDITY")
        return alerts
