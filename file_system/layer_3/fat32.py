from file_system.layer_2.nodeStream import *
from file_system.layer_2.node import *


class Fat32:
    def __init__(self, filename):
        self.filename = filename
        self.bootRecord = BootRecord(filename)
        self.fatTable = FatTable(self.bootRecord)
        self.dir_pre = DirectoryEntry(self.bootRecord)

    def BuildFileSystem(self):
        node_stream = NodeStream(self.filename)
        root_mgmt = NodeMgmt(["/", []])
        root_node = node_stream.make_node_stream("/", root_mgmt)
        return root_node