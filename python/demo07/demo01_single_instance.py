class A(object):
    pass
a = A()
print(a)
aa = A()
print(aa)

################################
class MusicPlayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

player00 = MusicPlayer()
print(player00)

player01 = MusicPlayer()
print(player01)

