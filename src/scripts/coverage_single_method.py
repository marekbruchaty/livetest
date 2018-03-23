import argparse
import subprocess
import xml.etree.ElementTree as element_tree

parser = argparse.ArgumentParser(description='Run single test case using pytest')

parser.add_argument('project_root', help='projects root path')
parser.add_argument('test_method', help='test method in the format <test_module>::<test_class>:<test_method>')

args = parser.parse_args()

project_root = args.project_root

if not str(project_root).startswith('/'):
    project_root += '/' + project_root

if not str(project_root).endswith('/'):
    project_root += project_root + '/'

output_file = project_root + "output.xml"

import coverage

cov = coverage.Coverage()
cov.start()

subprocess.check_output(["pytest", "-trace", project_root + args.test_method, "--junit-xml", output_file])

cov.stop()
cov.save()

cov.html_report()

tree = element_tree.parse(output_file)
root = tree.getroot()
test_suite = root.find('testsuite')
test_case = root.find('testcase')

file = test_case.get('file')
line = test_case.get('line')
name = test_case.get('name')
time = test_case.get('time')

print("file: " + file)
print("line: " + line)
print("name: " + name)
print("time: " + time)
