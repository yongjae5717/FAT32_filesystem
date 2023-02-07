import sys
# from file_system.layer_1.bootRecord import *
# from file_system.layer_1.DirectoryEntry import *
# from file_system.layer_1.fatTable import *
# from file_system.layer_2.node import *
# from file_system.layer_2.nodeStream import *
from file_system.Interface.dataStore import *
sys.setrecursionlimit(10 ** 6)


def main():

    """ exportPath, search_file format example
    search_file = "/DIR1/PORT.JPG"
    exportPath = "AllFiles"
    """
    # filename, exportPath = sys.argv[1], sys.argv[2]
    filename, filepath, exportPath = sys.argv[1], sys.argv[2], sys.argv[3]

    data_store = DataStore(filename)
    file_system = data_store.BuildFileSystem()
    file = file_system.GetNode(filepath)

    file.ExportTo(filename, exportPath)

if __name__ == "__main__":
    main()
