from file_system.layer_function.byteBuffer import *
from file_system.layer_function.file_io import *


class Boot_Record:
    def __init__(self, filename):
        self.filename = filename
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

    def make_boot_record(self):
        byte_array = ReadFile(self.filename, hex(0), hex(512))
        buffer = ByteBuffer(byte_array)
        buffer.jump(11)
        self.num_of_byte_per_sector = buffer.get_uint2_le()
        self.num_of_sector_per_cluster = buffer.get_data1()
        self.num_of_sector_reserved = buffer.get_uint2_le()
        self.num_of_FAT_area = buffer.get_data1()
        buffer.jump(19)
        self.num_of_sector_FAT_area = buffer.get_uint4_le()
        buffer.jump(4)
        self.cluster_num_of_root_dir = buffer.get_uint4_le()
        self.fat_region = self.num_of_sector_reserved * self.num_of_byte_per_sector
        self.data_region = self.fat_region + (self.num_of_FAT_area * self.num_of_sector_FAT_area * self.num_of_byte_per_sector)
        self.cluster_size = self.num_of_byte_per_sector * self.num_of_sector_per_cluster
        self.fat_size = self.num_of_sector_FAT_area * self.num_of_byte_per_sector
        self.fat_area_size = self.fat_size * self.num_of_FAT_area
