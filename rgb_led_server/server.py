from flask import Flask, render_template, request, jsonify
from gpioRgb import Rgbled


# -----------------------------
# Application setup
# -----------------------------


app = Flask(__name__)


# Initialize the RGB LED hardware (GPIO pins)
# anode=True for common anode RGB LED
led = Rgbled(17, 18, 27, annode=True)


# Store current LED state (shared state)
led_state = {
    "on": False,
    "color": (0, 0, 0),
    "color_name": "off"
}


# -----------------------------
# Web Page Route
# -----------------------------


@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------
# API Routes
# -----------------------------


@app.route("/api/status", methods=["GET"])
def api_status():
    """
    Return the current LED status
    """
    return jsonify(
        on=led_state["on"],
        color=list(led_state["color"]),
        color_name=led_state["color_name"]
    )


@app.route("/api/color", methods=["POST"])
def api_color():
    """
    Set the LED to a specific RGB color
    Expects JSON:
    { "color": [r, g, b] }
    """
    # Validate payload
    data = request.get_json(silent=True)

    if not data or "color" not in data:
        return jsonify(error="Missing color field"), 400

    try:
        r = int(data["color"][0])
        g = int(data["color"][1])
        b = int(data["color"][2])
    except (ValueError, TypeError, IndexError):
        return jsonify(error="Invalid color format"), 400

    # Set hardware
    led.set_color(r, g, b)



    # Set hardware
    led.set_color(r, g, b)


    # Determine color name (for dashboards)
    if (r, g, b) == (0, 0, 255):
        color_name = "blue"
    elif (r, g, b) == (0, 255, 0):
        color_name = "green"
    elif (r, g, b) == (255, 0, 0):
        color_name = "red"
    else:
        color_name = "custom"


    # Update shared state
    led_state["on"] = True
    led_state["color"] = (r, g, b)
    led_state["color_name"] = color_name


    return jsonify(success=True, color=color_name)


@app.route("/api/toggle", methods=["POST"])
def api_toggle():
    """
    Toggle the LED on or off
    """
    if led_state["on"]:
        led.turn_off()
        led_state["on"] = False
        led_state["color"] = (0, 0, 0)
        led_state["color_name"] = "off"
    else:
        led.set_color(255, 255, 255)
        led_state["on"] = True
        led_state["color"] = (255, 255, 255)
        led_state["color_name"] = "white"


    return jsonify(on=led_state["on"])


# -----------------------------
# Application Entry Point
# -----------------------------


if __name__ == "__main__":
    print("Starting RGB LED server...")


    # Startup test (safe)
    led.random_color()


    # Expose to network, disable reloader for GPIO safety
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )

