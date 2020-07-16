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
        print(end = '\n')

    def add(self, item):
        #头插法
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node
        #self.__head.prev = node
        #self.__head = node

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
            node.prev = cur

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
        cur = self.__head

        while cur!= None:
            if(cur.elem == item):
                #找到后判断是否为头节点
                if (cur == self.__head):
                    self.__head = cur.next
                    #特殊情况，判断是否只有一个节点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    #特殊情况，判断是最后一个节点
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


    def search(self, item):
        cur = self.__head
        while cur != None:
            if(cur.elem == item):
                return True
            else:
                cur = cur.next
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
