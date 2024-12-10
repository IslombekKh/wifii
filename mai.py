from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

led_state = "0"

@app.route("/")
def index():
    return f"""
    <html>
    <body>
        <h1>LED Controller</h1>
        <button onclick="toggleLED('1')">Turn ON</button>
        <button onclick="toggleLED('0')">Turn OFF</button>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.js"></script>
        <script>
            const socket = io();

            function toggleLED(state) {{
                socket.emit('change_led', state);
            }}
        </script>
    </body>
    </html>
    """

@socketio.on('change_led')
def handle_change_led(state):
    global led_state
    led_state = state
    emit('update_led', {'led_state': led_state}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
