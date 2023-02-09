class ClusterChain:
    def __init__(self, fatTable, bootRecord, first_cluster):
        self.fat_table = fatTable
        self.boot_record = bootRecord
        self.cluster_num = first_cluster
        self.cluster_list = list()

        self.free_cluster = '0x0000000'
        self.reserved_cluster = list(hex(i) for i in range(int('0xffffff0', 0), int('0xffffff6', 0) + 1))
        self.bad_cluster = '0xffffff7'
        self.eof = list(hex(i) for i in range (int ('0xffffff8', 0), int ('0xfffffff', 0) + 1))

    def make_cluster_list(self):
        while True:
            if self.cluster_num == len(self.fat_table.fat_table_list):
                break
            if self.fat_table.fat_table_list[self.cluster_num] in self.eof:
                break
            if self.fat_table.fat_table_list[self.cluster_num] == self.bad_cluster:
                continue
            cluster_offset = self.boot_record.data_region + (self.cluster_num - self.boot_record.cluster_num_of_root_dir) * self.boot_record.cluster_size
            if int('0x0000002', 0) <= self.cluster_num + 1 <= int('0xfffffef', 0):
                self.cluster_list.append((hex(cluster_offset), hex(self.boot_record.cluster_size)))
            self.cluster_num += 1
