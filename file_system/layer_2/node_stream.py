from file_system.layer_1.directoryEntry import *
from file_system.layer_1.bootRecord import *
from file_system.layer_1.fatTable import *
from file_system.layer_2.cluster_chain import *


class NodeStream:
    def __init__(self, filename):
        self.boot_record = BootRecord(filename)
        self.fat_table = FatTable(self.boot_record)
        self.dir_pre = DirectoryEntry(self.boot_record)
        self.boot_record.make_boot_record()
        self.fat_table.make_fat_table()
        self.dir_pre.data_area(self.boot_record.data_region)

    def make_node_stream(self, node_path, root_mgmt):
        for data in self.dir_pre.data_area_list:
            self.path = node_path
            if data.first_cluster >= len(self.fat_table.fat_table_list):
                continue
            if data.attribute == 16:
                self.path += data.name
                if self.path[-1] == ".":
                    continue
                self.dir_pre = DirectoryEntry(self.boot_record)
                self.dir_pre.data_area(data.dir_offset)
                root_mgmt.add([self.path, []])
                self.make_node_stream(self.path + "/", root_mgmt)

            elif data.attribute == 32:
                self.path += data.name + "." + data.extension
                cluster_n = ClusterChain(self.fat_table, self.boot_record, data.first_cluster)
                cluster_n.make_cluster_list()
                root_mgmt.add([self.path, cluster_n.cluster_list])
        return root_mgmt
