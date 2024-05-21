class person():

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
    
user = person.create()
print(user.display())

class monster():
    def attack(self, user):
        user.health = 10 - 5
        print (10)

