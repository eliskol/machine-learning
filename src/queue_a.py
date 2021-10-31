class Queue:

    def __init__(self, contents=None):

        if contents is None:
            self.contents = []

        else:
            self.contents = contents

    def print(self):

        for item in self.contents:

            print(item)

    def enqueue(self, item_to_queue):

        self.contents.append(item_to_queue)

    def dequeue(self):

        return self.contents.pop(0)
