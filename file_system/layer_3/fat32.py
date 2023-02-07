from file_system.layer_1.bootRecord import *
from file_system.layer_1.fatTable import *
from file_system.layer_2.nodeStream import *
from file_system.layer_2.node import *


class Fat32:
    def __init__(self, filename):
        self.filename = filename
        self.bootRecord = Boot_Record(filename)
        self.fatTable = fat_table(filename, self.bootRecord)
        self.dir_pre = DirectoryEntry(filename, self.bootRecord, self.bootRecord.data_region)

    def BuildFileSystem(self):
        root_mgmt = NodeMgmt(["/", []])
        NodeStream(self.filename, self.bootRecord, self.dir_pre, self.fatTable, "/", root_mgmt)
        return root_mgmt