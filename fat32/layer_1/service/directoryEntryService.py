from fat32.layer_1.domain.directoryEntry import *
from fat32.layer_1.domain.directoryEntryElements import *
from fat32.function.fileIo import *
from fat32.function.byteBuffer import *


class DirectoryEntryService:
    def __init__(self, filename):
        self.filename = filename
        self.directoryEntry = DirectoryEntry()

    def make_data_area(self, boot_record, dir_offset):
        offset = dir_offset
        while True:
            byte_array = read_file(self.filename, hex(offset), hex(32))
            offset += 32

            if byte_array == bytearray(
                    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'):
                break
            self.make_dir_entry(boot_record, byte_array)
        return self.directoryEntry

    def make_dir_entry(self, boot_record, byte_array):
            buffer = ByteBuffer(byte_array)
            DirElements = self.dir_entry_element(boot_record, buffer)
            self.directoryEntry.data_area_list.append(DirElements)

    def dir_entry_element(self, boot_record, buffer):
        name = buffer.get_ascii(8)
        extension = buffer.get_ascii(3)
        attribute = buffer.get_data1()
        buffer.jump(8)
        cluster_high = buffer.get_data2()
        buffer.jump(4)
        cluster_low = buffer.get_data2()
        first_cluster_buffer = ByteBuffer(cluster_low + cluster_high)
        first_cluster = first_cluster_buffer.get_uint4_le()
        dir_offset = boot_record.data_region + ((first_cluster - boot_record.cluster_num_of_root_dir) * boot_record.cluster_size)
        file_size = buffer.get_uint4_le()
        dir_elements = DirectoryEntryElements(name, attribute, first_cluster, dir_offset, file_size, extension)
        return dir_elements
