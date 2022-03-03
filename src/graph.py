from queue_a import Queue
from stack import *


class Graph:
    def __init__(self, edges):

        self.children_by_id = {edge[0]: [] for edge in edges}

        self.parents_by_id = {edge[1]: [] for edge in edges}

        for edge in edges:
            self.children_by_id[edge[0]].append(edge[1])
            self.parents_by_id[edge[1]].append(edge[0])

    def get_children(self, node):
        if node in self.children_by_id:
            return self.children_by_id[node]
        return None

    def get_parents(self, node):
        if node in self.parents_by_id:
            return self.parents_by_id[node]
        return None

    def breadth_first(self, node):
        queue = Queue([node])
        visited = {}
        order = []

        while queue.contents != []:

            dequeued_node = queue.dequeue()
            order.append(dequeued_node)
            visited[dequeued_node] = True

            node_children = self.get_children(dequeued_node)

            if node_children is None:
                continue

            for child in node_children:
                if child in visited:
                    continue
                queue.enqueue(child)
                visited[child] = True

        return order

    def depth_first(self, node):
        stack = Stack([node])
        visited = {}
        order = []

        while stack.contents != []:

            top_element = stack.pop()
            order.append(top_element)
            visited[top_element] = True

            top_element_children = self.get_children(top_element)

            if top_element_children is None:
                continue

            for child in top_element_children:
                if child in visited:
                    continue
                stack.push(child)
                visited[child] = True

        return order
