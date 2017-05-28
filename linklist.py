class node:
    def __init__(self):
        self.data = None
        self.next = None


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node()
        new_node.data = data
        print new_node.data
        new_node.next = self.cur_node
        print new_node.next
        self.cur_node = new_node

    def list_print(self):
        node = self.cur_node
        while node:
            print node.data
            node = node.next
            print node.next


ll = linked_list()
print ll
import pdb; pdb.set_trace()
ll.add_node(1)
print ll
ll.add_node(2)
print ll
ll.add_node(3)
print ll

ll.list_print()
