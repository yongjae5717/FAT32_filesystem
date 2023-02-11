import sys

from fat32.interface.dataStore import *


def main():
    """ exportPath, search_file format example
    search_file = "/DIR1/PORT.JPG"
    exportPath = "AllFiles"
    """

    try:
        filename, filepath, export_path = sys.argv[1], sys.argv[2], sys.argv[3]
    except IndexError as e:
        print(f'catch IndexError exception: {e}')
        exit()

    data_store = DataStore(filename)
    file_system = data_store.BuildFileSystem()
    file = file_system.get_node(filepath)
    file.export_to(filename, export_path)


if __name__ == "__main__":
    main()
