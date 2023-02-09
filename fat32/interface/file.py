from fat32.layer_2.domain.node import *
from fat32.function.fileIo import *


class File:
    def __init__(self, node):
        self.file = node

    def export_to(self, filename, exportPath):
        byte_array = bytearray()
        path, data = self.file.data
        destination_dir = os.path.join(exportPath, path[1:])

        for dir_offset, cluster_size in data:
            byte_array += read_file(filename, dir_offset, cluster_size)
        write_file(destination_dir, byte_array)