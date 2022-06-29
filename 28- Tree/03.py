class Tree_node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_lvl(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = "  " * self.get_lvl()
        prefix = spaces + "|--" if self.parent else "|--"
        print(prefix,self.data)
        for child in self.children:
            child.print_tree()
    def search(self, key):
        if self.data == key:
            return self
        for child in self.children:
            found = child.search(key)
            if found:
                return True
        return False

def create_tree():
    root = Tree_node("Electronics")

    laptop = Tree_node("Laptops")
    laptop.add_child(Tree_node("Apple"))
    laptop.add_child(Tree_node("Dell"))
    laptop.add_child(Tree_node("HP"))

    cell_phones = Tree_node("Cell Phones")
    cell_phones.add_child(Tree_node("Apple"))
    cell_phones.add_child(Tree_node("Samsung"))
    cell_phones.add_child(Tree_node("Nokia"))

    tv = Tree_node("Televisions")
    tv.add_child(Tree_node("Samsung"))
    tv.add_child(Tree_node("LG"))


    root.add_child(laptop)
    root.add_child(cell_phones)
    root.add_child(tv)

    return root


if __name__ == "__main__":
    root = create_tree()
    print(root.search("MSI"))