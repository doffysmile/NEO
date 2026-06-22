### MEMORIA
import json

def save_memory(user_input):
    data = {"command": user_input}
    with open("memory.json", "a") as file:
        file.write(json.dumps(data) + "\n")
