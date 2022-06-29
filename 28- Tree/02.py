class Tree_node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def print_tree(self, lvl=1):
        print(self.data)
        for child in self.children:
            print("   "*lvl, end="")
            child.print_tree(lvl+1)
    

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
    root.print_tree()