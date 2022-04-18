import glob
import xml.etree.ElementTree as ET


def merge_junit_results(xml_dirs, merged_file):
    failures = 0
    tests = 0
    errors = 0
    skipped = 0
    time = 0.0
    cases = []

    for file_name in glob.glob(xml_dirs + '/*.xml'):
        tree = ET.parse(file_name)
        test_suite = tree.getroot()
        failures += int(test_suite.attrib['failures'])
        tests += int(test_suite.attrib['tests'])
        errors += int(test_suite.attrib['errors'])
        skipped += int(test_suite.attrib['skipped'])
        time += float(test_suite.attrib['time'])
        for child in test_suite.iter():
            cases.append(child)

    new_root = ET.Element('testsuite')
    new_root.attrib['failures'] = '%s' % failures
    new_root.attrib['tests'] = '%s' % tests
    new_root.attrib['errors'] = '%s' % errors
    new_root.attrib['skipped'] = '%s' % skipped
    new_root.attrib['time'] = '%s' % time
    for case in cases:
        new_root.extend(case)
    new_tree = ET.ElementTree(new_root)
    new_tree.write(merged_file)

    return new_root.attrib


def get_junit_result(xml_file):
    tree = ET.parse(xml_file)

    return tree

