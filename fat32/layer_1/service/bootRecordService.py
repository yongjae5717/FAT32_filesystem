from fat32.function.fileIo import *
from fat32.function.byteBuffer import *
from fat32.layer_1.domain.bootRecord import *


class BootRecordService:
    def __init__(self, filename):
        self.filename = filename
        self.boot_record = BootRecord()

    def make_boot_record(self):
        byte_array = read_file(self.filename, hex(0), hex(512))
        buffer = ByteBuffer(byte_array)
        buffer.jump(11)
        num_of_byte_per_sector = buffer.get_uint2_le()
        num_of_sector_per_cluster = buffer.get_data1()
        num_of_sector_reserved = buffer.get_uint2_le()
        num_of_FAT_area = buffer.get_data1()
        buffer.jump(19)
        num_of_sector_FAT_area = buffer.get_uint4_le()
        buffer.jump(4)
        cluster_num_of_root_dir = buffer.get_uint4_le()
        fat_region = num_of_sector_reserved * num_of_byte_per_sector
        data_region = fat_region + (num_of_FAT_area * num_of_sector_FAT_area * num_of_byte_per_sector)
        cluster_size = num_of_byte_per_sector * num_of_sector_per_cluster
        fat_size = num_of_sector_FAT_area * num_of_byte_per_sector
        fat_area_size = fat_size * num_of_FAT_area
        self.boot_record.set_info(
            num_of_byte_per_sector, num_of_sector_per_cluster, num_of_sector_reserved, num_of_FAT_area,
            num_of_sector_FAT_area, cluster_num_of_root_dir, fat_region, data_region, cluster_size,
            fat_size, fat_area_size)
        return self.boot_record
