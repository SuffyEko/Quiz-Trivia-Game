import json

def load_file(filepath):
    try:

        with open(filepath) as load_file:
            content = load_file.read()
        if content:
            contain = json.loads(content)
        else:
            contain = []

        return contain
    except FileNotFoundError:
        return []
    except json.decoder.JSON.Decode.Error:
        return []

def save_file(data, filepath):
    with open(filepath, "w") as s_file:
        json.dump(data, s_file, indent=4)


def update_profile(name, score, highest_score):
    users = load_file("users.json")
    for user in users:
        if user['username'] == name:
            user['highest score'] = highest_score
            user['score'] = score

    save_file(users, "users.json")

    
