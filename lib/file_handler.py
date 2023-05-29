import os
import ebooklib.epub
import PyPDF2


def get_file_contents(filenames):
    files = []
    for file_name in filenames:
        # Initialize file path
        file_path = ""

        # Check if the file exists in the current directory
        if os.path.isfile(file_name):
            file_path = os.path.abspath(file_name)
        # Check if the full path is provided and the file exists at that location
        elif os.path.isfile(file_name) and os.path.isabs(file_name):
            file_path = file_name

        # Read file
        if file_path:
            try:
                if file_path.endswith('.epub'):
                    book = ebooklib.epub.read_epub(file_path)
                    title = book.get_metadata('DC', 'title')
                    try:
                        subtitle = title[1][0]
                    except IndexError:
                        subtitle = ""
                    title = title[0][0]
                    contents = ''
                    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
                        contents += item.get_content().decode('utf-8')
                    files.append({"filetype": "epub", "title": title, "contents": contents})

                else:
                    print(f"File type not supported: {file_path}")
                    exit(1)

            except Exception as e:
                print(f"Error reading file: {file_path}")
                print(str(e))
                exit(1)

        else:
            print(f"File not found: {file_name}")
            exit(1)
    return files


def duplicate_check(files, target_dir):
    duplicates = []
    for file in files:
        for filename in os.listdir(target_dir):
            if file["title"] in filename:
                duplicates.append(file)
    if len(duplicates):
        print("Found the following duplicates, skipping: \n{}".format(file["title"] for file in duplicates))
        return [file for file in files if file not in duplicates]
    return files
