from file_system.layer_function.byteBuffer import *


class DirectoryEntry:
    def __init__(self, filename, br, dir_offset):
        self.data_area_list = list()

        offset = dir_offset
        while True:
            with open(filename, 'rb') as f:
                f.seek(offset)
                byte_array = f.read(32)
            offset += 32

            if byte_array == bytearray (
                    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'):
                break

            buffer = ByteBuffer(byte_array)
            name = buffer.get_ascii(8)
            extension = buffer.get_ascii(3)
            attribute = int(byte_array[buffer.offset()])
            buffer.jump(9)
            cluster_high = buffer.get_data2()
            buffer.jump(4)
            cluster_low = buffer.get_data2()
            first_cluster_buffer = ByteBuffer(cluster_low + cluster_high)
            first_cluster = first_cluster_buffer.get_uint4_le()
            dir_offset = br.data_region + ((first_cluster - br.cluster_num_of_root_dir) * br.cluster_size)
            file_size = buffer.get_uint4_le()
            DirElements = DirectoryEntryElements(name, attribute, first_cluster, dir_offset, file_size, extension)

            self.data_area_list.append(DirElements)


class DirectoryEntryElements:
    def __init__(self, name, attribute, first_cluster, dir_offset, file_size, extension):
        self.name = name
        self.attribute = attribute
        self.first_cluster = first_cluster
        self.dir_offset = dir_offset
        self.file_size = file_size
        self.extension = extension
