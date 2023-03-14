import os
import sys

# parse cli args
def parse_cli_args():
    import argparse
    parser = argparse.ArgumentParser(description='process some cli args', usage='%(prog)s -f [file_path]')
    parser.add_argument('-f', nargs="?", type=str, help='path to a file')
    parser.add_argument('-v', help='verbose output', action='store_true')
    return parser.parse_args()

if __name__ == "__main__":
    # run: python3 cli_utils.py -v -f /tmp/test.txt
    print("[TEST] testing cli functions")
    args = parse_cli_args()
    print(f"[TEST] args: {args}")
    print(f"[TEST] args.f: {args.f}")
    print(f"[TEST] args.v: {args.v}")
