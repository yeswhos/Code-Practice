class MusicPlayer(object):
    instance = None
    flag = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        if MusicPlayer.flag is True:
            return
        print("init should appear once")
        MusicPlayer.flag = True

player00 = MusicPlayer()
print(player00)

player01 = MusicPlayer()
print(player01)