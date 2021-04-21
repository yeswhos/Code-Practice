class Node(object):
    '''
    节点
    '''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkedList(object):
    '''
    单链表
    '''
    def __init__(self, node = None):
        self.__head = node.elem

