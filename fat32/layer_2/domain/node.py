class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.path = ""