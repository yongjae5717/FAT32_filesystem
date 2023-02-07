from file_system.layer_2.node import *


class File:
    def __init__(self, node):
        self.file = node

    def ExportTo(self, filename, exportPath):
        byte_array = bytearray()
        path, data = self.file.data
        destination_dir = os.path.join(exportPath, path[1:])

        for dir_offset, cluster_size in data:
            byte_array += File.ReadFile(filename, dir_offset, cluster_size)
        File.WriteFile(destination_dir, byte_array)

    @classmethod
    def ReadFile(cls, filename, seek_offset, size):
        res = bytearray()
        with open(filename, 'rb') as f:
            f.seek(int(seek_offset, 16))
            res += f.read(int(size, 16))
        return res

    @classmethod
    def WriteFile(cls, destination_dir, byte_array):
        with open(destination_dir, "wb") as f:
            f.write(byte_array)
