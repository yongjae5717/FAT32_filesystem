class cluster_chain:
    def __init__(self, fatTable, first_cluster, dir_offset, cluster_num_of_root_dir, cluster_size):
        self.free_cluster = '0x0000000'
        self.reserved_cluster = list(hex(i) for i in range(int('0xffffff0', 0), int('0xffffff6', 0) + 1))
        self.bad_cluster = '0xffffff7'
        self.eof = list(hex(i) for i in range(int('0xffffff8', 0), int('0xfffffff', 0) + 1))

        self.cluster_num = first_cluster
        self.cluster_list = list()
        while True:
            if self.cluster_num == len(fatTable):
                break
            if fatTable[self.cluster_num] in self.eof:
                break
            if fatTable[self.cluster_num] == self.bad_cluster:
                continue
            cluster_offset = dir_offset + (self.cluster_num - cluster_num_of_root_dir) * cluster_size
            if int('0x0000002', 0) <= self.cluster_num + 1 <= int('0xfffffef', 0):
                self.cluster_list.append((hex(cluster_offset), hex(cluster_size)))
            self.cluster_num += 1
