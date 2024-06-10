import random
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

health = 20
damage = (random.choice(x))
age = (health - damage)
print("Your health is: "+str(age))

