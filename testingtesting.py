import random 
y =['you bump into a wall. ouch! try going the other way', 'OH NO A MONSTER',':>']             

class directions():
    def direction(self):
        direction = input('which way do you want to go, forward, left or right?')
        if direction == 'right':
            self.right
        if direction == 'left':
            self.left
        if direction == 'forward':
            self.forward
    def right(self):
        print('you move right')
        print(random.choice(y))
    def forward(self):
        print('you move forward')
        print(random.choice(y))
    def left(self):
        print('you move left')
        print(random.choice(y))

x = input("you wake up in the middle of the night, thirsty. do you want to get a glass of water?")
if x == 'yes':
    print('you get out of bed and open your door.')
    directions.direction()
    directions.direction()
 
