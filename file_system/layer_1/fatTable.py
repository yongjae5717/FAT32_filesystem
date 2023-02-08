from file_system.layer_function.byteBuffer import *
from file_system.layer_function.file_io import *


class fat_table:
    def __init__(self, br):
        self.br = br
        self.fat_table_list = list()

    def make_fat_table(self):

        offset = self.br.fat_region
        finish_count = self.br.num_of_sector_FAT_area // 4 + 1
        flag = 0
        self.repeat_offset_4(offset, finish_count, flag)

    def repeat_offset_4(self, offset, finish_count, flag):
        while flag != finish_count:
            byte_array = ReadFile(self.br.filename, hex(offset), hex(4))
            flag += 1
            offset += 4

            buffer = ByteBuffer(byte_array)

            be_byte_array = buffer.get_uint4_be()
            self.fat_table_list.append(be_byte_array)

