class Tool(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Tool.count += 1
    @classmethod
    def show_count(cls):
        print("被调用了 %d 次" % cls.count)

tool = Tool("sword")
tool.show_count()
