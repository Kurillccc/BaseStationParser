import json
import xml.etree.ElementTree as ET


def write_output_xml(root_elem, filename):
    tree = ET.ElementTree(root_elem)
    ET.indent(tree, space="    ", level=0)
    tree.write("output/" + filename, encoding="unicode")


def write_output_json(data, filename):
    with open("output/" + filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
