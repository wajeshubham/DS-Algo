class Stack:
    def __init__(self):
        self.container = []

    def is_empty(self):
        if len(self.container) == 0:
            return True
        return False

    def size(self):
        return len(self.container)

    def pop(self):
        if not self.is_empty():
            self.container.pop(-1)
            return
        print("stack is empty")

    def push(self, value):
        self.container.append(value)

    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        return "stack is empty"

    def print(self):
        for i in range(len(self.container) - 1, -1, -1):
            print("||", self.container[i], "||\n||=====||")
