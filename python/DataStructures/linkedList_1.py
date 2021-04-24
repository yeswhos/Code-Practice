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
        self.__head = node

    def isEmpty(self):
        if self.__head == None:
            return True
        return False

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        count = self.length()
        for i in range(count):
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        cur = self.__head
        node = Node(item)
        if self.isEmpty():
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        node = Node(item)
        pre = self.__head
        count = 0
        if pos == 0:
            self.add(item)
        elif pos == self.length():
            self.append(item)
        else:
            while count < pos - 1:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node


linked = SingleLinkedList()
# print('是否空', linked.isEmpty())
linked.append(1)
linked.travel()
# print(linked.length())
# print(linked.isEmpty())

linked.append(2)
linked.append(3)
linked.append(4)
linked.insert(2, 'new')
linked.travel()
