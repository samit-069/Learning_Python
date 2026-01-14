import json

def save_post(posts, file_name):
    with open(file_name, "w") as file:
        json.dump(posts, file)

def load_post(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}