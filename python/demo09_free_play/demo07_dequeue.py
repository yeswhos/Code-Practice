class Dequeue():
    def __init__(self):
        self.__list = []

    def add_front(self, val):
        self.__list.insert(0, val)

    def add_rear(self, val):
        self.__list.append(val)

    def pop_front(self):
        self.__list.pop(0)

    def pop_rear(self):
        self.__list.pop()


    def is_empty(self):
        return (self.__list == [])

    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    q = Dequeue()
    q.add_rear(1)
    q.add_front(2)

    print(q.pop_rear())
    print(q.pop_front())
