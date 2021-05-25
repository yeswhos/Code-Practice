class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        queue = []
        queue.append(self.root)
        if self.root is None:
            self.root = node
            return
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lChild is None:
                cur_node.lChild = node
                return
            else:
                queue.append(cur_node.lChild)
            if cur_node.rChild is None:
                cur_node.rChild = node
                return
            else:
                queue.append(cur_node.rChild)

    def breath_travel(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lChild is not None:
                queue.append(cur_node.lChild)
            if cur_node.rChild is not None:
                queue.append(cur_node.rChild)

    def preOrder(self, node):
        if node is None:
            return
        print(node.elem,end=" ")
        self.preOrder(node.lChild)
        self.preOrder(node.rChild)

    def midOrder(self, node):
        if node is None:
            return
        self.midOrder(node.lChild)
        print(node.elem,end=" ")
        self.midOrder(node.rChild)

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.lChild)
        self.postOrder(node.rChild)
        print(node.elem,end=" ")

tree = Tree()
tree.add('A')
tree.add('B')
tree.add('C')
tree.add('D')
tree.add('E')
tree.add('F')
tree.add('G')
tree.breath_travel()
print('\n')
tree.preOrder(tree.root)
print('\n')
tree.midOrder(tree.root)
print('\n')
tree.postOrder(tree.root)