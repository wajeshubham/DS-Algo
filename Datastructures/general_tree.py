class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        lvl = 0
        parent = self.parent
        while parent:
            lvl += 1
            parent = parent.parent
        return lvl

    def print(self):
        print(self.get_level() * "    " + "|-->", self.data)
        if len(self.children) != 0:
            for child in self.children:
                child.print()
