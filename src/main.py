import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(description="Data converter")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    args = parser.parse_args()
    return args

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    args = parse_args()
    data = load_json(args.input_file)
    save_json(data, args.output_file)
    print(f"Data saved to {args.output_file}")


