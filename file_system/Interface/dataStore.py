from file_system.Interface.fileSystem import *
from file_system.layer_3.fat32 import *


class DataStore:
    def __init__(self, filename):
        self.filename = filename

    def BuildFileSystem(self):
        fs = Fat32(self.filename)
        file_system = fs.BuildFileSystem()
        return FileSystem(file_system)