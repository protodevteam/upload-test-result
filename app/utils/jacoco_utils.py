import xml.etree.ElementTree as ET


def get_jacoco_result(xml_file):
    tree = ET.parse(xml_file)

    coverage = dict()
    for child in tree.getroot():
        if child.tag == 'counter':
            coverage[child.attrib['type']] = (child.attrib['missed'], child.attrib['covered'])

    return coverage
