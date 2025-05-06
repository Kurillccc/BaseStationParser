from app.bulder import build_tree, build_meta
from app.inputParser import parse_input
from app.writer import write_output_xml, write_output_json

if __name__ == "__main__":
    input_file = "input/impulse_test_input.xml"
    xml_output = "config.xml"
    json_output = "meta.json"

    classes, attributes, aggregations = parse_input(input_file)
    xml_tree = build_tree("BTS", attributes, aggregations)
    write_output_xml(xml_tree, xml_output)

    meta = build_meta(classes, attributes, aggregations)
    write_output_json(meta, json_output)
