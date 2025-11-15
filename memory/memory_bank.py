import os
import json

STORE = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'memory_bank.json')

class MemoryBank:
    def __init__(self):
        if os.path.exists(STORE):
            with open(STORE, 'r') as f:
                self.store = json.load(f)
        else:
            self.store = {}

    def save(self, key, value):
        self.store[key] = value
        with open(STORE, 'w') as f:
            json.dump(self.store, f, indent=2)

    def load(self, key):
        return self.store.get(key)
