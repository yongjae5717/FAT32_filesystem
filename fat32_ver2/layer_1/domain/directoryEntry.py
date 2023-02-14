class DirectoryEntry:
    def __init__(self):
        self.__data_area_list = list()

    def get_data_area_list(self):
        return self.__data_area_list

    def add(self, dir_elements):
        self.__data_area_list.append(dir_elements)
