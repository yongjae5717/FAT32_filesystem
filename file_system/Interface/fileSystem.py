from file_system.Interface.file import *


class FileSystem:
    def __init__(self, root_mgmt):
        self.file_system = root_mgmt

    def get_node(self, filePath):
        node = self.file_system.head
        while node.next:
            path, data = node.data
            if data and path == filePath:
                return File(node)
            node = node.next
        return -1
