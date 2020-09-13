class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]

    def get_paths(self):
        pass

# TODO implementation remaining


routes=[
    ("Mumbai","Dubai"),
    ("New York","Paris"),
    ("London","Paris"),
    ("Mumbai","Delhi"),
    ("Hydrabad","Delhi"),
    ("Mumbai","Pune"),
    ("Mumbai","Goa"),
    ("Goa","Dubai"),
]

graph=Graph(routes)
