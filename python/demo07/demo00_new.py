class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        #*元组 **字典
        print("new method")
        #为对象分配空间
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        print("inital")

player = MusicPlayer()
print(player)