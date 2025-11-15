import json
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'outputs')
if not os.path.exists(OUT):
    os.makedirs(OUT, exist_ok=True)

class SessionStore:
    def __init__(self):
        self.events = []

    def log_event(self, trace_id, name, payload):
        ev = {'trace_id': trace_id, 'name': name, 'payload': payload}
        self.events.append(ev)
        with open(os.path.join(OUT, 'session_events.json'), 'w') as f:
            json.dump(self.events, f, indent=2)
