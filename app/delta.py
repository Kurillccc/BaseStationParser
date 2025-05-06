import json


def generate_delta(config_path, patched_path, delta_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    with open(patched_path, 'r') as f:
        patched = json.load(f)

    additions = []
    deletions = []
    updates = []

    config_keys = set(config.keys())
    patched_keys = set(patched.keys())

    # additions - добавили в новую патч версию
    for key in patched_keys - config_keys:
        additions.append({"key": key, "value": patched[key]})

    # deletions - убрали из старой версии
    for key in config_keys - patched_keys:
        deletions.append(key)

    # updates - разница между новой и старой версией (измененные данные)
    for key in config_keys & patched_keys:
        if config[key] != patched[key]:
            updates.append({
                "key": key,
                "from": config[key],
                "to": patched[key]
            })

    delta = {
        "additions": additions,
        "deletions": deletions,
        "updates": updates
    }

    with open("output/" + delta_path, 'w') as f:
        json.dump(delta, f, indent=4)
