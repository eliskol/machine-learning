from queue_a import Queue
from stack import *
from node import Node
from graph import Graph


class WeightedGraph:
    def __init__(self, weights):
        self.edges = [edge for edge in weights]
        self.weights = weights
        self.children_by_id = {edge[0]: [] for edge in self.edges}

        self.parents_by_id = {edge[1]: [] for edge in self.edges}

        self.nodes_by_id = {}

        for edge in self.edges:
            if edge[0] not in self.nodes_by_id:
                self.nodes_by_id[edge[0]] = Node(edge[0])
            if edge[1] not in self.nodes_by_id:
                self.nodes_by_id[edge[1]] = Node(edge[1])
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


        queue = Queue([start_index])
        visited = {}
        order = []

        while queue.contents != []:

            dequeued_node = queue.dequeue()
            order.append(dequeued_node)
            visited[dequeued_node] = True
            node_children = self.get_children(dequeued_node)
            current_node = self.nodes_by_id[dequeued_node]

            if node_children is None:
                continue

            for child in node_children:
                if child in visited:
                    continue
                self.nodes_by_id[child].previous = current_node
                self.nodes_by_id[child].distance = current_node.distance + 1
                # print(self.nodes_by_id[child].distance)

                queue.enqueue(child)
                visited[child] = True
        return order

    def calc_distance(self, starting_node_index, ending_node_index):
        for id in self.nodes_by_id:
            self.nodes_by_id[id].distance = 999999999999
        current_node = starting_node_index
        current_node_obj = self.nodes_by_id[current_node]
        current_node_obj.distance = 0
        visited_nodes = []
        nodes_with_set_distance = {}

        while current_node != ending_node_index:
            if current_node in visited_nodes:
                nodes_with_set_distance.pop(current_node)
            visited_nodes.append(current_node)
            current_node_obj = self.nodes_by_id[current_node]

            for child in self.children_by_id[current_node]:
                if child in visited_nodes:
                    continue
                child_node_obj = self.nodes_by_id[child]
                edge = (current_node, child)
                child_node_obj.distance = min(
                    child_node_obj.distance, current_node_obj.distance + self.weights[edge])
                # print(child_node_obj.distance, child)
                nodes_with_set_distance[child] = child_node_obj.distance

            closest_node_to_start = min(nodes_with_set_distance, key=nodes_with_set_distance.get)

            current_node = closest_node_to_start

        return self.nodes_by_id[ending_node_index].distance

    def generate_shortest_path_graph(self):
        edges_for_graph = []
        for edge in self.edges:
            node_a_obj = self.nodes_by_id[edge[0]]
            node_b_obj = self.nodes_by_id[edge[1]]
            if node_b_obj.distance - node_a_obj.distance == self.weights[edge]:
                edges_for_graph.append(edge)

        return Graph(edges_for_graph)

    def calc_shortest_path(self, starting_node_index, ending_node_index):
        self.calc_distance(starting_node_index, ending_node_index)
        shortest_path_graph = self.generate_shortest_path_graph()
        return shortest_path_graph.calc_shortest_path(starting_node_index, ending_node_index)
