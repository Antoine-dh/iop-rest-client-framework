import sys
import argparse
from pathlib import Path
from .generator import generate_modules

def main(argv=None):
    parser = argparse.ArgumentParser(prog="iop_rest", description="Generate REST client and models dataclasses from OpenAPI spec")
    parser.add_argument("client_name", help="Classname of your REST client to be generated", type=Path)
    parser.add_argument("input_file", help="OpenAPI file", type=Path)
    parser.add_argument("output_path", help="Output directory", type=Path)
    args = parser.parse_args(argv[1:])
    generate_modules(args.client_name, args.input_file, args.output_path)

if __name__ == '__main__':
    main(sys.argv)
