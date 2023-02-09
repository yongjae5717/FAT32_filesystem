import sys

from fat32.interface.data_store import *


def main():
    """ exportPath, search_file format example
    search_file = "/DIR1/PORT.JPG"
    exportPath = "AllFiles"
    """
    filename, filepath, exportPath = sys.argv[1], sys.argv[2], sys.argv[3]

    data_store = DataStore(filename)
    file_system = data_store.BuildFileSystem()
    file = file_system.get_node(filepath)
    file.export_to(filename, exportPath)


if __name__ == "__main__":
    main()
