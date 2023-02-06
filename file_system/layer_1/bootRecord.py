from file_system.layer_function.byteBuffer import *


class Boot_Record:
    def __init__(self, filename):
        with open(filename, 'rb') as f:
            byte_array = f.read(512)
        buffer = ByteBuffer(byte_array)
        buffer.jump(11)
        self.num_of_byte_per_sector = buffer.get_uint2_le()
        self.num_of_sector_per_cluster = int(byte_array[buffer.offset()])
        buffer.jump(1)
        self.num_of_sector_reserved = buffer.get_uint2_le()
        self.num_of_FAT_area = int(byte_array[buffer.offset()])
        buffer.jump(20)
        self.num_of_sector_FAT_area = buffer.get_uint4_le()
        buffer.jump(4)
        self.cluster_num_of_root_dir = buffer.get_uint4_le()
        self.fat_region = self.num_of_sector_reserved * self.num_of_byte_per_sector
        self.data_region = self.fat_region + (self.num_of_FAT_area * self.num_of_sector_FAT_area * self.num_of_byte_per_sector)
        self.cluster_size = self.num_of_byte_per_sector * self.num_of_sector_per_cluster
        self.fat_size = self.num_of_sector_FAT_area * self.num_of_byte_per_sector
        self.fat_area_size = self.fat_size * self.num_of_FAT_area
        print(hex(self.num_of_byte_per_sector))
        print(hex(self.num_of_sector_per_cluster))
        print(hex(self.num_of_sector_reserved))
        print(hex(self.num_of_FAT_area))
        print(hex(self.num_of_sector_FAT_area))
        print(hex(self.cluster_num_of_root_dir))
        print(hex(self.fat_region))
        print(hex(self.data_region))
        print(hex(self.cluster_size))
        print(hex(self.fat_size))
        print(hex(self.fat_area_size))