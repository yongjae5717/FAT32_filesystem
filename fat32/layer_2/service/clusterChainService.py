from fat32.layer_2.domain.clusterChain import *


class ClusterChainService:
    def __init__(self, first_cluster):
        self.cluster_chain = ClusterChain(first_cluster)

    def make_cluster_list(self, fat_table, boot_record):
        while True:
            if self.cluster_chain.cluster_num == len(fat_table.fat_table_list):
                break
            if fat_table.fat_table_list[self.cluster_chain.cluster_num] in self.cluster_chain.eof:
                break
            if fat_table.fat_table_list[self.cluster_chain.cluster_num] == self.cluster_chain.bad_cluster:
                continue
            cluster_offset = boot_record.data_region + (self.cluster_chain.cluster_num - boot_record.cluster_num_of_root_dir) * boot_record.cluster_size
            if int('0x0000002', 0) <= self.cluster_chain.cluster_num + 1 <= int('0xfffffef', 0):
                self.cluster_chain.cluster_list.append((hex(cluster_offset), hex(boot_record.cluster_size)))
            self.cluster_chain.cluster_num += 1
        return self.cluster_chain
    