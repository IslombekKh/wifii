from flask import Flask, jsonify, request

app = Flask(__name__)

# LED holatini saqlash
led_state = "0"

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>ESP8266 LED Controller</title> 
    </head>
    <body>
        <h1>ESP8266 LED Controller</h1>
        <button onclick="fetch('/led/on').then(() => location.reload())">LED ON</button>
        <button onclick="fetch('/led/off').then(() => location.reload())">LED OFF</button>
        <p>LED State: {led_state}</p>
    </body>
    </html>
    """

@app.route("/led/<state>", methods=["GET"])
def control_led(state):
    global led_state
    if state == "on":
        led_state = "1"
    elif state == "off":
        led_state = "0"
    return jsonify({"led_state": led_state})

@app.route("/state", methods=["GET"])
def get_state():
    return jsonify({"led_state": led_state})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
