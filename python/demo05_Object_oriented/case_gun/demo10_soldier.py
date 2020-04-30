from case_gun.demo09_gun import ak47


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if (self.gun == None):
            print("%s has no gun" % self.name)
        self.gun.add_bullet(30)
        self.gun.shoot()

FBI = Soldier("FBI")
FBI.gun = ak47
FBI.fire()
print(FBI.gun)