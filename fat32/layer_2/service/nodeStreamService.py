from fat32.layer_2.domain.nodeStream import *
from fat32.layer_1.service.directoryEntryService import *
from fat32.layer_2.service.clusterChainService import *


class NodeStreamService:
    def __init__(self, filename):
        self.node_stream = NodeStream()
        self.filename = filename

    def make_node_stream(self, boot_record, fat_table, directory_entry, node_path):
        for data in directory_entry.data_area_list:
            self.node_stream.path = node_path
            if data.first_cluster >= len(fat_table.fat_table_list):
                continue
            if data.attribute == 16:
                self.node_stream.path += data.name
                if self.node_stream.path[-1] == ".":
                    continue
                directory_entry_service = DirectoryEntryService(self.filename)
                directory_entry = directory_entry_service.make_data_area(boot_record, data.dir_offset)
                self.node_stream.root_mgmt.add([self.node_stream.path, []])
                self.make_node_stream(boot_record, fat_table, directory_entry, self.node_stream.path + "/")

            elif data.attribute == 32:
                self.node_stream.path += data.name + "." + data.extension
                cluster_chain_service = ClusterChainService (data.first_cluster)
                cluster_n = cluster_chain_service.make_cluster_list(fat_table, boot_record)
                self.node_stream.root_mgmt.add([self.node_stream.path, cluster_n.cluster_list])
        return self.node_stream.root_mgmt
