import random 
y =['you bump into a wall. ouch! try going the other way', 'OH NO A MONSTER',':>']             

class directions():
    def direction(self):
        direction = input('which way do you want to go, forward, left or right?')
        if direction == 'right':
            print('you move right')
            print(random.choice(y))
        if direction == 'left':
            print('you move left')
            print(random.choice(y))
        if direction == 'forward':
            print('you move forward')
            print(random.choice(y))


x = directions()
x.direction()
