import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(description="Data converter")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print(f"Input: {args.input_file}, Output: {args.output_file}")

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    args = parse_args()
    data = load_json(args.input_file)
    print(f"Data: {data}")
