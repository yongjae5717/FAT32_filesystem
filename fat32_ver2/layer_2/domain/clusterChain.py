class ClusterChain:
    def __init__(self, first_cluster):
        self.__cluster_num = first_cluster
        self.__cluster_list = list()

        self.__free_cluster = '0x0000000'
        self.__reserved_cluster = list(hex(i) for i in range(int('0xffffff0', 0), int('0xffffff6', 0) + 1))
        self.__bad_cluster = '0xffffff7'
        self.__eof = list(hex(i) for i in range (int ('0xffffff8', 0), int ('0xfffffff', 0) + 1))

    def get_cluster_num(self):
        return self.__cluster_num

    def plus_cluster_num(self):
        self.__cluster_num += 1

    def get_cluster_list(self):
        return self.__cluster_list

    def get_free_cluster(self):
        return self.__free_cluster

    def get_reserved_cluster(self):
        return self.__reserved_cluster

    def get_bad_cluster(self):
        return self.__bad_cluster

    def get_eof(self):
        return self.__eof

    def add(self, cluster_offset, cluster_size):
        self.__cluster_list.append((hex(cluster_offset), hex(cluster_size)))
