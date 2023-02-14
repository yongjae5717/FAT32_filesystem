import os
from fat32_ver2.function.fileIo import *
from fat32_ver2.layer_2.domain.node import *


class NodeService:
    def __init__(self):
        self.node_mgmt = NodeMgmt(data=None)

    def set_node_mgmt(self, data):
        self.node_mgmt = NodeMgmt(data)

    def add(self, data):
        if self.node_mgmt.head == "":
            self.node_mgmt.head = Node(data)
        else:
            node = self.node_mgmt.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def all_files_export(self, filename, exportPath):
        node = self.node_mgmt.head
        while node.next:
            path, data = node.data
            destination_dir = os.path.join(exportPath,  path[1:])
            if not os.path.exists(destination_dir) and not data:
                os.makedirs(destination_dir)
            elif data:
                byte_array = bytearray()
                for dir_offset, cluster_size in data:
                    byte_array += read_file (filename, dir_offset, cluster_size)
                    write_file(destination_dir, byte_array)

            node = node.next

    def selected_file_export(self, filename, dataPath, exportPath):
        node = self.node_mgmt.head
        while node.next:
            path, data = node.data
            destination_dir = os.path.join(exportPath,  path[1:])

            if not os.path.exists(destination_dir) and not data:
                os.makedirs(destination_dir)
            elif data and path == dataPath:
                byte_array = bytearray()
                for dir_offset, cluster_size in data:
                    byte_array += read_file(filename, dir_offset, cluster_size)
                write_file(destination_dir, byte_array)
                break

            node = node.next
