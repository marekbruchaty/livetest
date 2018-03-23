import argparse
import subprocess

parser = argparse.ArgumentParser(description='Detect test methods')

parser.add_argument('project_root', help='project root path')

args = parser.parse_args()
project_root = args.project_root

out = subprocess.check_output(['pytest', '-q', args.project_root, '--collect-only'])

for item in out.decode('utf-8').splitlines():
    print("item: " + item)
    split_item = item.split('::')
    if len(split_item) < 3:
        continue
    test_module = split_item[0]
    test_class = split_item[1]
    test_method = split_item[2]

    print("Test .... ")
    print("test_module: " + test_module)
    print("test_class: " + test_class)
    print("test_method: " + test_method)
