print('ON NO THERE IS A MONSTER')

import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




class person():
    def __init__(self, health):
        self.health = health
        self.damage = random.choice(numbers)

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
    
   


    def __str__(self):
        
        print(f'my attack power is {self.health - self.damage}')
    
user = person.create()
print(user.display())

class monster():

    def attack(self, user):
        user.health = 10 - 5
        print ("user.health")
        




    def __str__(self):
        return f"{self.name}, {self.age}, {self.artist}"