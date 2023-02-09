from fat32.layer_1.domain.fatTable import *
from fat32.function.fileIo import *
from fat32.function.byteBuffer import *


class FatTableService:
    def __init__(self, filename):
        self.filename = filename
        self.fat_table = FatTable()

    def make_fat_table(self, boot_record):

        offset = boot_record.fat_region
        finish_count = boot_record.num_of_sector_FAT_area // 4 + 1
        flag = 0
        self.repeat_offset_4(offset, finish_count, flag)
        return self.fat_table

    def repeat_offset_4(self, offset, finish_count, flag):
        while flag != finish_count:
            byte_array = read_file(self.filename, hex(offset), hex(4))
            flag += 1
            offset += 4

            buffer = ByteBuffer(byte_array)

            be_byte_array = buffer.get_uint4_be()
            self.fat_table.fat_table_list.append(be_byte_array)
