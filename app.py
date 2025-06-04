# app.py
from flask import Flask, jsonify
from collections import Counter
import threading
import keyboard

app = Flask(__name__)
key_counter = Counter()

# Background thread to track keys
def track_keys():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key_counter[event.name] += 1

@app.route('/keys', methods=['GET'])
def get_keys():
    return jsonify(key_counter)

if __name__ == '__main__':
    threading.Thread(target=track_keys, daemon=True).start()
    app.run(debug=True, port=5000)
