class LinkedList(object):
    def __init__(self, head=None):
        self.count: int
        self.count = 0
    def get_count(self):
        return self.get_count
    
    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data);
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val);
        # TODO: find the first item with a given value
        item = self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None;



    def deleteAt(self, index)
        # TODO: delete an item at given index
        if index > self.count-1:
            return
        if index == 0:
            self.head = self.head.get_next()
        else:
            tempIndex = 0
            node = self.head
            while tempIndex < index -1:
                node = node.get_next()
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
    while (tempnode != None)
        print("Node: ", tempnode_get_data())
        tempnode = tempnode.get_next()

#create a linked list and insert some items
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)
itemList.dump_list()

#   exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ",itemlist.find(13))
print("Finding item: ", itemlist.find(78))

#delete an item
itemlist.delete(3)
print("item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(3))
itemlist.dump_list()