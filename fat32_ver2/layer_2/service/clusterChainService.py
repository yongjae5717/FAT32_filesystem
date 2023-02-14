from fat32_ver2.layer_2.domain.clusterChain import *


class ClusterChainService:
    def __init__(self, first_cluster):
        self.cluster_chain = ClusterChain(first_cluster)

    def make_cluster_list(self, fat_table, boot_record):
        while True:
            table_list = fat_table.get_fat_table_list()
            if self.cluster_chain.get_cluster_num() == len(table_list):
                break
            if table_list[self.cluster_chain.get_cluster_num()] in self.cluster_chain.get_eof():
                break
            if table_list[self.cluster_chain.get_cluster_num()] == self.cluster_chain.get_bad_cluster():
                continue
            cluster_offset = boot_record.get_data_region() + (self.cluster_chain.get_cluster_num() - boot_record.get_cluster_num_of_root_dir()) * boot_record.get_cluster_size()
            if int('0x0000002', 0) <= self.cluster_chain.get_cluster_num() + 1 <= int('0xfffffef', 0):
                self.cluster_chain.add(cluster_offset, boot_record.get_cluster_size())

            self.cluster_chain.plus_cluster_num()
        return self.cluster_chain
    