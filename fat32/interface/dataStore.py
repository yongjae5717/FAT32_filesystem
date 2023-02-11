from fat32.layer_3.service.fatSystemService import *
from fat32.interface.fileSystem import *


class DataStore:
    def __init__(self, filename):
        self.filename = filename

    def BuildFileSystem(self):
        fs = FatSystemService(self.filename)
        file_system = fs.BuildFileSystem()
        return FileSystem(file_system)
