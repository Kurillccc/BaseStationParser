import json


def apply_delta(config_path, delta_path, result_path):
    with open(config_path, 'r') as f:
        config = json.load(f)

    with open(delta_path, 'r') as f:
        delta = json.load(f)

    # Удаления
    for key in delta.get("deletions", []):
        config.pop(key, None)

    # Обновления
    for update in delta.get("updates", []):
        config[update["key"]] = update["to"]

    # Добавления
    for addition in delta.get("additions", []):
        config[addition["key"]] = addition["value"]

    # Сохраняем результат
    with open("output/" + result_path, 'w') as f:
        json.dump(config, f, indent=4)
