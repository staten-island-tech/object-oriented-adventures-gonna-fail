print('ON NO THERE IS A MONSTER')

import random
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class person():

    def __init__(self, name, age, gender):
        self.damage = random.choice(x)
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def create():
        name = input("enter your characters name")
        age = int(input("enter characters age"))
        gender = (input("enter characters gender"))
        return person(name, age, gender)
        

user = person.create()
print(user.display())

def battle(self, monster):
    self.health = health
    monster.health = monster.health - self.damage
    print(monster.health)
    health = 20
    monster = random.choice()
    y = health - monster
    print(y)
    battle(monster)

    




