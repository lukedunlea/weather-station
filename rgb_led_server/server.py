from flask import Flask, render_template, request, jsonify
from gpioRgb import Rgbled

# Create the Flask application
app = Flask(__name__)

# Initialize the RGB LED hardware (GPIO pins)
# anode=True for common anode RGB LED
led = Rgbled(17, 18, 27, annode=True)

# Keep track of the current LED state
led_state = {
    "on": False,
    "color": (0, 0, 0)
}

# -----------------------------
# Web Page Route
# -----------------------------

@app.route("/")
def index():
    """Serve the main web page"""
    return render_template("index.html")

# -----------------------------
# API Routes
# -----------------------------

@app.route("/api/status", methods=["GET"])
def api_status():
    """
    Return the current LED status
    Example response:
    { "color": [255, 0, 0], "on": true }
    """
    return jsonify(
        color=list(led_state["color"]),
        on=led_state["on"]
    )

@app.route("/api/color", methods=["POST"])
def api_color():
    """
    Set the LED to a specific RGB color
    Expects JSON: { r: int, g: int, b: int }
    """
    data = request.json

    r = int(data["r"])
    g = int(data["g"])
    b = int(data["b"])

    led.set_color(r, g, b)

    led_state["on"] = True
    led_state["color"] = (r, g, b)

    return jsonify(success=True)

@app.route("/api/toggle", methods=["POST"])
def api_toggle():
    """
    Toggle the LED on or off
    Returns: { on: true/false }
    """
    if led_state["on"]:
        led.turn_off()
        led_state["on"] = False
        led_state["color"] = (0, 0, 0)
    else:
        led.set_color(255, 255, 255)
        led_state["on"] = True
        led_state["color"] = (255, 255, 255)

    return jsonify(on=led_state["on"])

# -----------------------------
# Application Entry Point
# -----------------------------

if __name__ == "__main__":
    print("Starting server and testing LED...")

    # Simple startup test to confirm hardware works
    led.random_color()

    # IMPORTANT: Disable reloader for GPIO safety
    app.run(debug=False, use_reloader=False)
