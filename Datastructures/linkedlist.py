class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # initially head of linked list will be None (empty)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node  # after inserting our new node will be our linked list's head because we are inserting at
        # the beginning

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def append_values(self, array):  # this will join a the array to existing linked list
        for i in array:
            self.insert_at_end(i)

    def insert_values(self,
                      array):  # this will create a new linked list with on the values passed in the place of array
        self.head = None
        for i in array:
            self.insert_at_end(i)

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.length():
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if index - 1 == count:
                itr.next = Node(data, itr.next)
                break
            count += 1
            itr = itr.next

    def reverse(self):
        count = 0
        itr = self.head
        for _ in range(self.length()):
            if count <= self.length():
                self.delete(count)
                self.insert_at_beginning(itr.data)
            itr = itr.next
            count += 1

    def index_of(self, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return count
            count += 1
            itr = itr.next
        return f"{data} does not exist"

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.data) + " --->"
            itr = itr.next
        print(llist)

    def delete(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if index - 1 == count:  # stop at the previous element
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next
