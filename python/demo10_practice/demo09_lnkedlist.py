class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class singleLinkedList(object):
    def __init__(self, node = None):
        self.__head = node

    def is_empty(self):
        if self.__head == None:
            return True
        else:
            return False

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def append(self, item):
        node = Node(item)
        cur = self.__head
        while cur.next != None:
            cur = cur.next
        cur.next = node

singleInstance = singleLinkedList()
# singleInstance.append(10)
# singleInstance.travel()
singleInstance.travel()
print(singleInstance.is_empty())