
class person():
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health
    damage = 10
    health = 20

    x = health - damage
    print(f"You have encountered {x}")
