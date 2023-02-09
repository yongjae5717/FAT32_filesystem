from fat32.layer_2.domain.node import *


class NodeStream:
    def __init__(self):
        self.path = "/"
        self.root_mgmt = NodeMgmt(["/", []])