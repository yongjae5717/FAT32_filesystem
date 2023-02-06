from file_system.layer_1.DirectoryEntry import *
from file_system.layer_2.cluster_chain import *


class DirFileRead:
    def __init__(self, filename, br, dir_pre, fatTable, node_path, root_mgmt):
        for data in dir_pre.data_area_list:
            self.path = node_path
            if data.first_cluster >= len(fatTable.fat_table_list):
                continue
            print(data.name, data.extension)

            if data.attribute == 16:
                self.path += data.name
                if self.path[-1] == ".":
                    continue
                dir_pre = DirectoryEntry(filename, br, data.dir_offset)
                root_mgmt.add([self.path, []])
                DirFileRead(filename, br, dir_pre, fatTable, self.path + "/", root_mgmt)

            elif data.attribute == 32:
                self.path += data.name + "." + data.extension
                cluster_n = cluster_chain(fatTable.fat_table_list, data.first_cluster, br.data_region,
                                         br.cluster_num_of_root_dir, br.cluster_size)
                root_mgmt.add([self.path, cluster_n.cluster_list])
