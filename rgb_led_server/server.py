from flask import Flask, render_template, render_template, request, jsonify #imported flask to make server
from gpioRgb import Rgbled

app = Flask(__name__) #creats the flask application

#initializes the GPIO pins
led = Rgbled(17, 18, 27, annode=True)

# this is keeping track of the state of the LED
led_state = {
    "on": False,
    "color": (0, 0, 0)
}

@app.route('/') # runs this code when someone visits the webpage
def index():
    return render_template("index.html")

@app.route("/turn_on", methods=["POST"])
def turn_on():
    led.set_color(100, 100, 100)
    led_state["on"] = True
    led_state["color"] = (100, 100, 100)
    return jsonify(success=True, state=led_state)

@app.route("/led/off", methods=["POST"])
def led_off():
    led.turn_off()
    return jsonify(success=True, state="off")



@app.route("/led/color", methods=["POST"])
def led_color():
    data = request.json
    r = int(data["r"])
    g = int(data["g"])
    b = int(data["b"])

    led.set_color(r, g, b)
    return jsonify(success=True, color=(r, g, b))



if __name__ == '__main__':
    print("Starting server and testing LED...")
    
    led.random_color()
    app.run(debug=True, use_reloader=False) #this is important because leds cant handle two requests at once.