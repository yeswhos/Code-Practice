class Queue():
    def __init__(self):
        self.__list = []

    def enqueue(self, val):
        self.__list.insert(0, val)

    def dequeue(self):
        return self.__list.pop()

    def is_empty(self):
        return (self.__list == [])

    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())