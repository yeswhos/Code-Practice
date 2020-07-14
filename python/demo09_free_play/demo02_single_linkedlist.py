class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node = None):
        self.__head = node

    def is_empty(self):
        # cur = self._head
        # if cur:
        #     return True
        # else:
        #     return False
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next

    def add(self, item):
        #头插法
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        #尾插法
        #创建节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass

node = Node(100)
single_obj = SingleLinkList()

if __name__ == "__main__":
    linked = SingleLinkList()
    print(linked.is_empty())
    print(linked.length())
    linked.append(10)
    linked.add(20)
    print(linked.is_empty())
    print(linked.length())
    linked.travel()
