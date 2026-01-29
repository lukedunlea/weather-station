from flask import Flask, render_template
from thermosensor import ThermoSensor  # Import my Day 7 Thermo sensor
from routes.sensor_routes import create_sensor_routes

app = Flask(__name__)

# Initialise the hardware component when the server starts
sensor = ThermoSensor()

# register the sensor API routes
app.register_blueprint(create_sensor_routes(sensor))

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Simple test to confirm the sensor works on startup
    print("Current temperature:", sensor.read_temperature())

    # Start the Flask web server
    app.run(host="0.0.0.0", port=5000, debug=True)


