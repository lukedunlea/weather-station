from flask import Blueprint, jsonify

def create_sensor_routes(sensor):
    # Group sensor-related routes
    sensor_bp = Blueprint("sensor", __name__)

    @sensor_bp.route("/api/sensor")
    def get_sensor_data():
        # Read the sensor and return the data as JSON
        return jsonify(sensor.read_temperature())

    # Return the routes so they can be registered in app.py
    return sensor_bp
