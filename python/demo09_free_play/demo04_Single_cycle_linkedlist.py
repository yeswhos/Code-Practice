class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node = None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end = " ")
            cur = cur.next
        print(cur.elem)
        #print(end = '\n')

    def add(self, item):
        #头插法
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next

        node.next = self.__head
        self.__head = node
        cur.next = self.__head

    def append(self, item):
        #尾插法
        #创建节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            #或者 node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """
        :param pos: 从0开始
        :param item: 插入的元素
        :return: 并不return，插进去就好了
        """
        if pos <= 0:
            self.add(item)
        elif(pos > (self.length() - 1)):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if(cur.elem == item):
                #找到后判断是否为头节点
                if (cur == self.__head):
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre.next = cur.next

        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if(cur.elem == item):
                return True
            else:
                cur = cur.next
        #因为最后一个节点不会到循环里，所以单独拿出来弄
        if cur.elem == item:
            return True
        return False

node = Node(100)
single_obj = SingleLinkList()

if __name__ == "__main__":
    linked = SingleLinkList()
    linked.append(10)
    linked.add(20)
    print(linked.is_empty())
    print(linked.length())
    linked.travel()
    linked.insert(1, 30)
    linked.travel()
    # print(linked.search(40))
    linked.remove(20)
    linked.travel()
