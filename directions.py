

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

import random 
y =['you bump into a wall. ouch! try going the other way', 'OH NO A MONSTER',':>']             

class directions():
    def direction(self, y):
        direction = input('which way do you want to go, forward, left or right?')
        print(f'you moved {direction}')
        print(random.choice(y))


x = directions()
a = input("you wake up in the middle of the night, thirsty. do you want to get a glass of water?")
if a == 'yes':
    print('you get out of bed and open your door.')
    monster = x.direction(y)
    #if monster then call monster fight stuff
    if random.choice(y) == 'OH NO A MONSTER':
        x.people(y)
    x.direction(y)
    x.direction(y)
    print('you move forward and approach the staircase. carefully you walk down stairs, so you dont trip and fall')
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    print('you move left and move into your kitchen! you succesfully acquire a glass of water and turn to go back to bed.')
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    x.direction(y)
    print('you move forward and approach the staircase. carefully you walk up stairs, so you dont trip and fall')
    x.direction(y)
    x.direction(y)
    x.direction(y)
    print('you take a sip of water, set it aside and then go back to sleep')
if a == 'no':
    print('goodbye')
elif:
    print('retry')