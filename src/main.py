import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Data converter")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print(f"Input: {args.input_file}, Output: {args.output_file}")
