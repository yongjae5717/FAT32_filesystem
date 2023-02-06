import sys
from file_system.layer_1.bootRecord import *
from file_system.layer_1.DirectoryEntry import *
from file_system.layer_1.fatTable import *
from file_system.layer_2.node import *
from file_system.layer_2.dir_file_read import *
sys.setrecursionlimit(10 ** 6)


def main():

    """ exportPath, search_file format example
    search_file = "/DIR1/PORT.JPG"
    exportPath = "AllFiles"
    """
    filename, exportPath = sys.argv[1], sys.argv[2]
    # filename, search_file, exportPath = sys.argv[1], sys.argv[2], sys.argv[3]

    br = Boot_Record(filename)
    fatTable = fat_table(filename, br)
    dir_pre = DirectoryEntry(filename, br, br.data_region)

    root_mgmt = NodeMgmt(["/", []])
    DirFileRead(filename, br, dir_pre, fatTable, "/", root_mgmt)
    root_mgmt.all_files_export(filename, exportPath)
    # root_mgmt.selected_file_export(filename, search_file, exportPath)


if __name__ == "__main__":
    main()
