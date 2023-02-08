from file_system.layer_2.node import *
from file_system.layer_function.file_io import *


class File:
    def __init__(self, node):
        self.file = node

    def ExportTo(self, filename, exportPath):
        byte_array = bytearray()
        path, data = self.file.data
        destination_dir = os.path.join(exportPath, path[1:])

        for dir_offset, cluster_size in data:
            byte_array += read_file(filename, dir_offset, cluster_size)
        write_file(destination_dir, byte_array)