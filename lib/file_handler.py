import os
import ebooklib.epub
import PyPDF2


def get_file_contents(filenames):
    file_contents = []
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
                # Check file extension and read accordingly
                if file_path.endswith('.pdf'):
                    with open(file_path, 'rb') as file:
                        reader = PyPDF2.PdfFileReader(file)
                        contents = ''
                        for page in range(reader.getNumPages()):
                            contents += reader.getPage(page).extractText()
                        file_contents.append({"filetype": "pdf", "contents": contents})

                elif file_path.endswith('.epub'):
                    book = ebooklib.epub.read_epub(file_path)
                    contents = ''
                    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
                        contents += item.get_content().decode('utf-8')
                    file_contents.append({"filetype": "epub", "contents": contents})

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
    return file_contents
