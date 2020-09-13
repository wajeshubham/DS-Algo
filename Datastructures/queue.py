from collections import deque

"""Using a list"""


class Queue:
    def __init__(self):
        self.container = []

    def is_empty(self):
        if len(self.container) == 0:
            return True
        return False

    def length(self):
        return len(self.container)

    def enqueue(self, data):
        if self.is_empty():
            self.container.append(data)
            return
        self.container.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        self.container.pop(-1)

    def print(self):
        if self.is_empty():
            return "Queue is empty"
        for i in range(len(self.container)):
            print(" === \n|", self.container[i], "|")


"""using a deque"""


class QueueD:
    def __init__(self):
        self.container = deque()

    def is_empty(self):
        if len(self.container) == 0:
            return True
        return False

    def length(self):
        return len(self.container)

    def enqueue(self, data):
        self.container.appendleft(data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        self.container.pop()

    def print(self):
        if self.is_empty():
            return "Queue is empty"
        for i in range(len(self.container)):
            print(" === \n|", self.container[i], "|")
