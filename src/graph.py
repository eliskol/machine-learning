class Graph:
    def __init__(self, edges):

        self.children_by_id = {edge[0] : [] for edge in edges}

        self.parents_by_id = {edge[1] : [] for edge in edges}
        
        for edge in edges:
            self.children_by_id[edge[0]].append(edge[1])
            self.parents_by_id[edge[1]].append(edge[0])


    def get_children(self, node):
        return self.children_by_id[node]


    def get_parents(self, node):
        return self.parents_by_id[node]


oog = Graph([[0, 1], (1, 2), [2, 0]])
print(oog.get_children(2))