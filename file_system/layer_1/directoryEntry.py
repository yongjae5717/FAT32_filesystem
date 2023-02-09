from file_system.layer_function.byte_buffer import *
from file_system.layer_function.file_io import *


class DirectoryEntry:
    def __init__(self, boot_record):
        self.data_area_list = list()
        self.boot_record = boot_record

    def data_area(self, dir_offset):
        offset = dir_offset
        while True:
            byte_array = read_file(self.boot_record.filename, hex(offset), hex(32))
            offset += 32

            if byte_array == bytearray (
                    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'):
                break
            self.fat32_data_area(byte_array)

    def fat32_data_area(self, byte_array):
            buffer = ByteBuffer(byte_array)
            DirElements = self.make_dirEntryElements (buffer)
            self.data_area_list.append(DirElements)

    def make_dirEntryElements(self, buffer):
        name = buffer.get_ascii(8)
        extension = buffer.get_ascii(3)
        attribute = buffer.get_data1()
        buffer.jump(8)
        cluster_high = buffer.get_data2()
        buffer.jump(4)
        cluster_low = buffer.get_data2()
        first_cluster_buffer = ByteBuffer (cluster_low + cluster_high)
        first_cluster = first_cluster_buffer.get_uint4_le ()
        dir_offset = self.boot_record.data_region + ((first_cluster - self.boot_record.cluster_num_of_root_dir) * self.boot_record.cluster_size)
        file_size = buffer.get_uint4_le ()
        dir_elements = DirectoryEntryElements (name, attribute, first_cluster, dir_offset, file_size, extension)
        return dir_elements


class DirectoryEntryElements:
    def __init__(self, name, attribute, first_cluster, dir_offset, file_size, extension):
        self.name = name
        self.attribute = attribute
        self.first_cluster = first_cluster
        self.dir_offset = dir_offset
        self.file_size = file_size
        self.extension = extension
