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
x.direction(y)
x.direction(y)