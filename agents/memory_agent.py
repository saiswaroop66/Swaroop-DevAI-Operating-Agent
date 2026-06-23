import json
import os

MEMORY_FILE = "memory.json"


def load_memory():

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    return {}


def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def add_fact(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def get_fact(key):

    memory = load_memory()

    return memory.get(key)


def get_all_memory():

    return load_memory()