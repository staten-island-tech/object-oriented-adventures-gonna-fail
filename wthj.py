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
        print(f"Name: {self.age}")
        print(f"Name: {self.gender}")

    def create():
        name = input("enter your characters name")
        age = int(input("enter characters age"))
        gender = (input("enter characters gender"))
        return person(name, age, gender)
    
    User = create()
    print(User.display())
