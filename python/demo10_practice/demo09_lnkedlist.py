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
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self, item):
        cur = self.__head
        while cur != None:
            if (cur.elem == item):
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self.__head
        pre = None

        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head == cur.next
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur
                cur = cur.next

singleInstance = singleLinkedList()
singleInstance.append(10)
singleInstance.add(20)
singleInstance.add(20)
#print(singleInstance.length())
singleInstance.insert(2, 30)
print(singleInstance.search(30))
singleInstance.remove(10)
singleInstance.travel()
# singleInstance.travel()
# print(singleInstance.is_empty())