class Stack:

    def __init__(self, contents=None):

        if contents is None:
            self.contents = []

        else:
            self.contents = contents

    def print(self):

        for item in self.contents[::-1]:

            print(item)

    def push(self, item_to_push):

        self.contents.append(item_to_push)

    def pop(self):
        return self.contents.pop()
