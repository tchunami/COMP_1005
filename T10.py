class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:   
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def print_bst(self):
        if self.left:
            self.left.print_bst()
        print(self.value)
        if self.right:
            self.right.print_bst()


# Tutorial 10:

def search_tree(Node, element):
    # First base-case: 
    if Node is None:
        print(f"Node {element} is not found")
        return Node
    
    # Second base-case: 
    if Node.value == element:
        print(f"Node {element} is found")
        return Node

    # Recursive:
    if Node.value > element: 
        search_tree(Node.left, element) 
    elif Node.value < element: 
        search_tree(Node.right, element)

def main():
    root = Node(25)
    root.insert(19)
    root.insert(28)
    root.insert(13)
    root.insert(9)
    root.insert(30)
    root.insert(17)
    root.insert(26)
    root.print_bst()

    # in the tree
    search_bst(root, 19)
    # not in the tree
    search_bst(root, 7)
    
if __name__ == "__main__":
   main()