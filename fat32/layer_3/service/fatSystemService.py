from fat32.layer_1.service.bootRecordService import *
from fat32.layer_1.service.fatTableService import *
from fat32.layer_2.service.nodeStreamService import *


class FatSystemService:
    def __init__(self, filename):
        self.boot_record_service = BootRecordService(filename)
        self.fat_table_service = FatTableService (filename)
        self.node_stream_service = NodeStreamService (filename)
        self.directory_entry_service = DirectoryEntryService (filename)

    def BuildFileSystem(self):
        self.boot_record = self.boot_record_service.make_boot_record ()
        self.fat_table = self.fat_table_service.make_fat_table (self.boot_record)
        self.directory_entry = self.directory_entry_service.make_data_area (self.boot_record, self.boot_record.data_region)
        self.node_stream = self.node_stream_service.make_node_stream (self.boot_record, self.fat_table, self.directory_entry,
                                                            self.node_stream_service.node_stream.path)
        return self.node_stream