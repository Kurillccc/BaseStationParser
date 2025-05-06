from app.bulder import build_tree, build_meta
from app.inputParser import parse_input
from app.writer import write_output_xml, write_output_json
from app.delta import generate_delta

if __name__ == "__main__":
    input_file = "input/impulse_test_input.xml"
    config = "input/config.json"
    patched_config = "input/patched_config.json"
    xml_output = "config.xml"
    json_output = "meta.json"
    delta = "delta.json"

    classes, attributes, aggregations = parse_input(input_file)

    xml_tree = build_tree("BTS", attributes, aggregations)
    write_output_xml(xml_tree, xml_output)

    meta = build_meta(classes, attributes, aggregations)
    write_output_json(meta, json_output)

    generate_delta(config, patched_config, delta)
