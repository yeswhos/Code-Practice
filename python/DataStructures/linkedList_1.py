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
    def length(self):
        cur = self.__head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self.__head
        count = self.length()
        for i in range(count):
            print(cur.elem)
            cur = cur.next
