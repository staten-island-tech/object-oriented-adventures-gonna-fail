print('ON NO THERE IS A MONSTER')

import random
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class person():
    def __init__(self, health):
        self.health = health
        self.damage = random.choice(x)
        health = 20
        damage = (random.choice(x))
        age = (health - damage)
        print("Your health is: "+str(age))

    def __init__(self, name, age, gender):
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
    def battle(self, monster):
        monster.age = monster.health - self.damage
        print(monster.age)
    


    def __str__(self):
        
        print(f'my attack power is {self.health - self.damage}')
    
user = person.create()
print(user.display())

