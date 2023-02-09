class BootRecord:
    def __init__(self):
        self.num_of_byte_per_sector = 0
        self.num_of_sector_per_cluster = 0
        self.num_of_sector_reserved = 0
        self.num_of_FAT_area = 0
        self.num_of_sector_FAT_area = 0
        self.cluster_num_of_root_dir = 0
        self.fat_region = 0
        self.data_region = 0
        self.cluster_size = 0
        self.fat_size = 0
        self.fat_area_size = 0

    def set_info(self, num_of_byte_per_sector, num_of_sector_per_cluster, num_of_sector_reserved, num_of_FAT_area,
                 num_of_sector_FAT_area, cluster_num_of_root_dir, fat_region, data_region, cluster_size, fat_size,
                 fat_area_size):
        self.num_of_byte_per_sector = num_of_byte_per_sector
        self.num_of_sector_per_cluster = num_of_sector_per_cluster
        self.num_of_sector_reserved = num_of_sector_reserved
        self.num_of_FAT_area = num_of_FAT_area
        self.num_of_sector_FAT_area = num_of_sector_FAT_area
        self.cluster_num_of_root_dir = cluster_num_of_root_dir
        self.fat_region = fat_region
        self.data_region = data_region
        self.cluster_size = cluster_size
        self.fat_size = fat_size
        self.fat_area_size = fat_area_size

    def __str__(self):
        return f'Boot Record: \n' \
               f'num_of_byte_per_sector: {hex(self.num_of_byte_per_sector)}\n' \
               f'num_of_sector_per_cluster: {hex(self.num_of_sector_per_cluster)}\n' \
               f'num_of_sector_reserved: {hex(self.num_of_sector_reserved)}\n' \
               f'num_of_FAT_area: {hex(self.num_of_FAT_area)}\n' \
               f'num_of_sector_FAT_area: {hex(self.num_of_sector_FAT_area)}\n' \
               f'cluster_num_of_root_dir: {hex(self.cluster_num_of_root_dir)}\n' \
               f'fat_region: {hex(self.fat_region)}\n' \
               f'data_region: {hex(self.data_region)}\n' \
               f'cluster_size: {hex(self.cluster_size)}\n' \
               f'fat_size: {hex(self.fat_size)}\n' \
               f'fat_area_size: {hex(self.fat_area_size)}\n'
