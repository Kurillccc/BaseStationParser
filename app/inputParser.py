import xml.etree.ElementTree as ET
from collections import defaultdict


def parse_input(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    classes = {}
    attributes = defaultdict(list)
    aggregations = defaultdict(list)

    # Чтение классов и атрибутов
    for elem in root.findall('Class'):
        class_name = elem.attrib['name']
        classes[class_name] = {
            "documentation": elem.attrib.get("documentation", ""),
            "isRoot": elem.attrib.get("isRoot", "false") == "true"
        }
        for attr in elem.findall('Attribute'):
            attributes[class_name].append((attr.attrib['name'], attr.attrib['type']))

    # Чтение агрегаций
    for agg in root.findall('Aggregation'):
        src = agg.attrib['source']
        tgt = agg.attrib['target']
        src_mult = agg.attrib['sourceMultiplicity']
        aggregations[tgt].append((src, src_mult))

    return classes, attributes, aggregations
