class Tree_node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    



if __name__ == "__main__":
    root = Tree_node("Electronics")
    laptop = Tree_node("Laptop")
    root.add_child(laptop)