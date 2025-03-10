import json


def load_settings():
    with open('game_data.json', 'r') as file:
        data = json.load(file)

    return data


def update_settings():
    with open('game_data.json', 'w') as file:
        json.dump(settings, file, indent=2, ensure_ascii=False)
        file.flush()  # to force immediate write to disk


settings = load_settings()
