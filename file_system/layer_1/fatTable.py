from file_system.layer_function.byte_buffer import *
from file_system.layer_function.file_io import *


class FatTable:
    def __init__(self, boot_record):
        self.boot_record = boot_record
        self.fat_table_list = list()

    def make_fat_table(self):

        offset = self.boot_record.fat_region
        finish_count = self.boot_record.num_of_sector_FAT_area // 4 + 1
        flag = 0
        self.repeat_offset_4(offset, finish_count, flag)

    def repeat_offset_4(self, offset, finish_count, flag):
        while flag != finish_count:
            byte_array = read_file(self.boot_record.filename, hex(offset), hex(4))
            flag += 1
            offset += 4

            buffer = ByteBuffer(byte_array)

            be_byte_array = buffer.get_uint4_be()
            self.fat_table_list.append(be_byte_array)

