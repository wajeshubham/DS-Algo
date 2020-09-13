class HashMap:
    def __init__(self):
        self.max_length = 10
        self.arr = [[] for _ in range(self.max_length)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max_length

    def __setitem__(self, key, value):
        k = self.get_hash(key)

        for i in range(len(self.arr[k])):
            if self.arr[k][i][0] == key:
                self.arr[k][i][1] = value
                return
        self.arr[k].append([key, value])

    def __getitem__(self, item):
        k = self.get_hash(item)
        for i in range(len(self.arr[k])):
            if self.arr[k][i][0] == item:
                return self.arr[k][i][1]
        return f"{item} does not exist"

    def __delitem__(self, key):
        k = self.get_hash(key)
        for i in range(len(self.arr[k])):
            if self.arr[k][i][0] == key:
                del self.arr[k][i]
                break
