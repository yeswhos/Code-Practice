class Game(object):
    top_score = 0
    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print("attack")

    @classmethod
    def show_top_score(cls):
        print(Game.top_score)

    def start_game(self):
        print("开始")

Game.show_help()
Game.show_top_score()
game = Game("Fanhui")
game.start_game()