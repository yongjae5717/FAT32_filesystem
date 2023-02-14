class BootRecord:
    def __init__(self):
        self.__num_of_byte_per_sector = 0
        self.__num_of_sector_per_cluster = 0
        self.__num_of_sector_reserved = 0
        self.__num_of_FAT_area = 0
        self.__num_of_sector_FAT_area = 0
        self.__cluster_num_of_root_dir = 0
        self.__fat_region = 0
        self.__data_region = 0
        self.__cluster_size = 0
        self.__fat_size = 0
        self.__fat_area_size = 0

    def set_info(self, num_of_byte_per_sector, num_of_sector_per_cluster, num_of_sector_reserved, num_of_FAT_area,
                 num_of_sector_FAT_area, cluster_num_of_root_dir, fat_region, data_region, cluster_size, fat_size,
                 fat_area_size):
        self.__num_of_byte_per_sector = num_of_byte_per_sector
        self.__num_of_sector_per_cluster = num_of_sector_per_cluster
        self.__num_of_sector_reserved = num_of_sector_reserved
        self.__num_of_FAT_area = num_of_FAT_area
        self.__num_of_sector_FAT_area = num_of_sector_FAT_area
        self.__cluster_num_of_root_dir = cluster_num_of_root_dir
        self.__fat_region = fat_region
        self.__data_region = data_region
        self.__cluster_size = cluster_size
        self.__fat_size = fat_size
        self.__fat_area_size = fat_area_size

    def get_num_of_byte_per_sector(self):
        return self.__num_of_byte_per_sector

    def set_num_of_byte_per_sector(self, value):
        self.__num_of_byte_per_sector = value

    def get_num_of_sector_per_cluster(self):
        return self.__num_of_sector_per_cluster

    def set_num_of_sector_per_cluster(self, value):
        self.__num_of_sector_per_cluster = value

    def get_num_of_sector_reserved(self):
        return self.__num_of_sector_reserved

    def set_num_of_sector_reserved(self, value):
        self.__num_of_sector_reserved = value

    def get_num_of_FAT_area(self):
        return self.__num_of_FAT_area

    def set_num_of_FAT_area(self, value):
        self.__num_of_FAT_area = value

    def get_num_of_sector_FAT_area(self):
        return self.__num_of_sector_FAT_area

    def set_num_of_sector_FAT_area(self, value):
        self.__num_of_sector_FAT_area = value

    def get_cluster_num_of_root_dir(self):
        return self.__cluster_num_of_root_dir

    def set_cluster_num_of_root_dir(self, value):
        self.__cluster_num_of_root_dir = value

    def get_fat_region(self):
        return self.__fat_region

    def set_fat_region(self, value):
        self.__fat_region = value

    def get_data_region(self):
        return self.__data_region

    def set_data_region(self, value):
        self.__data_region = value

    def get_cluster_size(self):
        return self.__cluster_size

    def set_cluster_size(self, value):
        self.__cluster_size = value

    def get_fat_size(self):
        return self.__fat_size

    def set_fat_size(self, value):
        self.__fat_size = value

    def get_fat_area_size(self):
        return self.__fat_area_size

    def set_fat_area_size(self, value):
        self.__fat_area_size = value

    def __str__(self):
        return f'Boot Record: \n' \
               f'num_of_byte_per_sector: {hex(self.__num_of_byte_per_sector)}\n' \
               f'num_of_sector_per_cluster: {hex(self.__num_of_sector_per_cluster)}\n' \
               f'num_of_sector_reserved: {hex(self.__num_of_sector_reserved)}\n' \
               f'num_of_FAT_area: {hex(self.__num_of_FAT_area)}\n' \
               f'num_of_sector_FAT_area: {hex(self.__num_of_sector_FAT_area)}\n' \
               f'cluster_num_of_root_dir: {hex(self.__cluster_num_of_root_dir)}\n' \
               f'fat_region: {hex(self.__fat_region)}\n' \
               f'data_region: {hex(self.__data_region)}\n' \
               f'cluster_size: {hex(self.__cluster_size)}\n' \
               f'fat_size: {hex(self.__fat_size)}\n' \
               f'fat_area_size: {hex(self.__fat_area_size)}\n'
