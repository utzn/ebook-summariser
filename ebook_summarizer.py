import argparse

from lib.file_handler import get_file_contents


def main(args):
    file_contents = get_file_contents(args)
    print("Hi")
    # scan_books(file_contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is a script that checks if a file exists.')
    parser.add_argument('file_names', type=str, nargs='+', help='One or more file names or full paths to the files.')

    args = parser.parse_args()
    main(args.file_names)
