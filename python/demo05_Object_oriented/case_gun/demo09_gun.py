class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if(self.bullet_count <= 0):
            print("%s no bullet" % self.model)
            return
        self.bullet_count -= 1
        print("%s biubiubiu" % self.model)
        print("left bullet: %s" % self.bullet_count)

ak47 = Gun("ak47")
# ak47.add_bullet(30)
# ak47.shoot()
