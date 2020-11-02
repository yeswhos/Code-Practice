class Node(object):
    def __init__(self, name):
        self._children = []
        self.name = name
    def __repr__(self):
        return "<node '{}'>".format(self.name)
    def append(self, *args, **kwargs):
        self._children.append(*args, **kwargs)

    def depth_first(self):
        print(self)
        for child in self._children:
            child.depth_first()

    def breath_first(self):
        def gen(o):
            all = [o, ]
            while all:
                next = all.pop()
                all.extend(next._children)
                yield next

            for node in gen(self):
                print(node)

root = Node("root")
child_1 = Node("child1")
child_2 = Node("child2")
child_3 = Node("child3")
child_4 = Node("child4")
child_5 = Node("child5")