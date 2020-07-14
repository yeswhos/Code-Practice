class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node = None):
        self._head = node

    def is_empty(self):
        # cur = self._head
        # if cur:
        #     return True
        # else:
        #     return False
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        pass

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
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
    linked.append(20)
    print(linked.is_empty())
    print(linked.length())
    linked.travel()
