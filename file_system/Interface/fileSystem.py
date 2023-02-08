from file_system.Interface.file import *


class FileSystem:
    def __init__(self, root_mgmt):
        self.file_system = root_mgmt

    def GetNode(self, filePath):
        node = self.file_system.head
        while node.next:
            path, data = node.data
            print(path, filePath)
            if data and path == filePath:
                return File(node)
            node = node.next
        return -1
