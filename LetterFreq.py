import argparse
import os

def valid_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"Path '{path}' does not exist.")
    return path

parser = argparse.ArgumentParser()
parser.add_argument(
    "--file", type=valid_path, help="Path to file that the program process", required=True
)
args = parser.parse_args()


with open(args.file, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)