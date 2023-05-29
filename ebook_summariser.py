import argparse
import os
import sys

from lib.file_handler import get_file_contents, duplicate_check


def main(args):
    files = get_file_contents(args.file_names)
    files = duplicate_check(files, args.target_dir)

    print("Adding the following books:")
    print([file["title"] for file in files])
    print("Stop")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is a script that checks if a file exists.')
    parser.add_argument('file_names', type=str, nargs='+', help='One or more file names or full paths to the files.')
    parser.add_argument('target_dir', type=str, help='Target directory in which to create Markdown files.')

    args = parser.parse_args()

    if os.path.isdir(args.target_dir):
        main(args)
    else:
        print("Target directory {} does not exist".format(args.target_dir))
        sys.exit(1)
