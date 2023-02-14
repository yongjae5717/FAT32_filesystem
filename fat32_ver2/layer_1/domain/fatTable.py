class FatTable:
    def __init__(self):
        self.__fat_table_list = list()

    def get_fat_table_list(self):
        return self.__fat_table_list

    def add(self, byte_array):
        self.__fat_table_list.append(byte_array)
