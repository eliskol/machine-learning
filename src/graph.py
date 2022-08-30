from queue_a import Queue
from stack import *
from node import Node


class Graph:
    def __init__(self, edges):

        self.children_by_id = {edge[0]: [] for edge in edges}

        self.parents_by_id = {edge[1]: [] for edge in edges}

        self.nodes_by_id = {}

        for edge in edges:
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

    def set_distance_and_previous(self, start_index):

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
        self.set_distance_and_previous(starting_node_index)
        ending_node = self.nodes_by_id[ending_node_index]
        if ending_node_index not in self.set_distance_and_previous(starting_node_index):
            return False
        else:
            return self.nodes_by_id[ending_node_index].distance

    def calc_shortest_path(self, starting_node_index, ending_node_index):
        self.set_distance_and_previous(starting_node_index)

        if self.calc_distance(starting_node_index, ending_node_index) is False:
            return False

        path = [ending_node_index]
        current_node = self.nodes_by_id[ending_node_index]
        goal_node = self.nodes_by_id[starting_node_index]

        while current_node != goal_node:
            current_node = current_node.previous
            path.append(current_node.id)
        return path[::-1]

    def cycle_algo(self, current_node_index, starting_node_index, visited=[]):
        visited.append(current_node_index)
        if current_node_index in self.children_by_id.keys():
            for node_index in self.children_by_id[current_node_index]:
                print(current_node_index)
                if node_index in visited:
                    print(node_index)
                    return True
                else:
                    return self.cycle_algo(node_index, starting_node_index, visited)
        else:
            return False

    def check_for_cycle(self):
        for node_index in self.children_by_id:
            if self.cycle_algo(node_index, node_index) is True:
                return True
            else:
                continue
        return False
