class Node(object):
    def __init__(self, item):
        self.elem = item
        self.rChild = None
        self.lChild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        # queue = []
        # queue.append(self.root)
        queue = [self.root]
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
        queue = [self.root]
        while queue:
            cur_node = queue.pop()
            print(cur_node.elem)
            if cur_node.lChild is not None:
                queue.append(cur_node.lChild)
            if cur_node.rChild is not None:
                queue.append(cur_node.rChild)
    def preOrder(self, node):
        if node is None:
            return
        print(node.elem, end=" ")
        self.preOrder(node.lChild)
        self.preOrder(node.rChild)

    def midOrder(self, node):
        if node is None:
            return

        self.preOrder(node.lChild)
        print(node.elem, end=" ")
        self.preOrder(node.rChild)
    def postOrder(self, node):
        if node is None:
            return

        self.preOrder(node.lChild)
        self.preOrder(node.rChild)
        print(node.elem, end=" ")


tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.breath_travel()
tree.preOrder(tree.root)
tree.midOrder(tree.root)
tree.postOrder(tree.root)