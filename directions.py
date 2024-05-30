import random 
y =['you bump into a wall. ouch! try going the other way', 'OH NO A MONSTER',':>']             

class directions():
    def direction(self):
        direction = input('which way do you want to go, forward, left or right?')
        if direction == 'right':
            self.right()
        if direction == 'left':
            self.left
        if direction == 'forward':
            self.forward
    def right():
        print('you move right')
        print(random.choice(y))
    def forward():
        print('you move forward')
        print(random.choice(y))
    def left():
        print('you move left')
        print(random.choice(y))

directions.forward()
