from file_system.layer_1.DirectoryEntry import *
from file_system.layer_1.bootRecord import *
from file_system.layer_1.fatTable import *
from file_system.layer_2.cluster_chain import *


class NodeStream:
    def __init__(self, filename):
        self.bootRecord = Boot_Record(filename)
        self.fatTable = fat_table(self.bootRecord)
        self.dir_pre = DirectoryEntry(self.bootRecord)
        self.bootRecord.make_boot_record()
        self.fatTable.make_fat_table()
        self.dir_pre.data_area(self.bootRecord.data_region)

    def make_node_stream(self, node_path, root_mgmt):
        for data in self.dir_pre.data_area_list:
            self.path = node_path
            if data.first_cluster >= len(self.fatTable.fat_table_list):
                continue
            if data.attribute == 16:
                self.path += data.name
                if self.path[-1] == ".":
                    continue
                self.dir_pre = DirectoryEntry(self.bootRecord)
                self.dir_pre.data_area(data.dir_offset)
                root_mgmt.add([self.path, []])
                self.make_node_stream(self.path + "/", root_mgmt)

            elif data.attribute == 32:
                self.path += data.name + "." + data.extension
                cluster_n = cluster_chain(self.fatTable, self.bootRecord, data.first_cluster)
                cluster_n.make_cluster_list()
                # cluster_n = cluster_chain(self.fatTable.fat_table_list, data.first_cluster, self.bootRecord.data_region,
                #                           self.bootRecord.cluster_num_of_root_dir, self.bootRecord.cluster_size)
                root_mgmt.add([self.path, cluster_n.cluster_list])
        return root_mgmt
