class Stack:
    def __init__(self):
        self.elements = []

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        return self.elements.pop()

    def top(self):
        if len(self.elements) != 0:
            return self.elements[-1]
        return None

    def __str__(self):
        return f"Stack({self.elements})"

    def __len__(self):
        return len(self.elements)
