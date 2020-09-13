class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def previous_of(self, data):
        if data == self.head.data:
            return None

        itr = self.head
        while itr:
            if itr.data == data:
                return itr.prev.data
            itr = itr.next
        return f"{data} does not exist"

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return

        node = Node(data, self.head, None)
        self.head = node
        node.next.prev = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data, None, itr)
                break
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = Node(data, self.head, None)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next, itr)
                itr.next.next.prev = itr.next
                break
            count += 1
            itr = itr.next

    def append_values(self, array):
        for i in array:
            self.insert_at_end(i)

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                return
            count += 1
            itr = itr.next

    def index_of(self, data):
        if data == self.head.data:
            return 0

        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                return count
            count += 1
            itr = itr.next
        return f"{data} does not exist"

    def remove_by_value(self, data):
        if self.head.data == data:
            self.remove_at(0)
            return

        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(self.index_of(itr.data))
                return
            itr = itr.next

    def length(self):
        if self.head is None:
            return 0

        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        dllist = ""
        while itr:
            dllist += str(itr.data) + "<--->"
            itr = itr.next
        print(dllist)
