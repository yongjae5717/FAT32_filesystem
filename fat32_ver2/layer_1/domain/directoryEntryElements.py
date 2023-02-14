class DirectoryEntryElements:
    def __init__(self, name, attribute, first_cluster, dir_offset, file_size, extension):
        self.__name = name
        self.__attribute = attribute
        self.__first_cluster = first_cluster
        self.__dir_offset = dir_offset
        self.__file_size = file_size
        self.__extension = extension

    def get_name(self):
        return self.__name

    def get_attribute(self):
        return self.__attribute

    def get_first_cluster(self):
        return self.__first_cluster

    def get_dir_offset(self):
        return self.__dir_offset

    def get_file_size(self):
        return self.__file_size

    def get_extension(self):
        return self.__extension
