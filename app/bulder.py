import xml.etree.ElementTree as ET
from collections import defaultdict


def build_meta(classes, attributes, aggregations):
    # Выстраиваем обратную агрегацию
    reverse_agg = defaultdict(list)
    mult_map = {}

    for parent, children in aggregations.items():
        for child, multiplicity in children:
            reverse_agg[child].append(parent)
            min_val, max_val = (multiplicity.split("..") + [multiplicity])[:2]
            mult_map[(child, parent)] = {"min": min_val, "max": max_val}

    # Построение метаинформации
    result = []
    for class_name, meta in classes.items():
        entry = {
            "class": class_name,
            "documentation": meta["documentation"],
            "isRoot": meta["isRoot"],
            "parameters": []
        }

        # Добавляем обычные параметры
        for name, typ in attributes.get(class_name, []):
            entry["parameters"].append({"name": name, "type": typ})

        # Добавляем классы-агрегации
        for child, mult in aggregations.get(class_name, []):
            entry["parameters"].append({"name": child, "type": "class"})

        # Добавляем min/max только если это не root
        if not meta["isRoot"]:
            parents = reverse_agg.get(class_name, [])
            if parents:
                parent = parents[0]
                mult = mult_map.get((class_name, parent), {"min": "1", "max": "1"})
                entry["min"] = mult["min"]
                entry["max"] = mult["max"]

        result.append(entry)

    result.sort(key=lambda x: (x["class"] == "BTS", len(x["parameters"])))
    return result


def build_tree(root_name, attributes, aggregations, visited=None):
    if visited is None:
        visited = set()

    if root_name in visited:
        return None  # Защита от циклов

    visited.add(root_name)
    elem = ET.Element(root_name)

    for attr_name, attr_type in attributes.get(root_name, []):
        child = ET.SubElement(elem, attr_name)
        child.text = attr_type

    for child_name, _ in aggregations.get(root_name, []):
        child_elem = build_tree(child_name, attributes, aggregations, visited)
        if child_elem is not None:
            elem.append(child_elem)

    return elem
