import random 
y =['you bump into a wall. ouch! try going the other way', 'OH NO A MONSTER',':>']             

class directions():
    def direction(self, y):
        direction = input('which way do you want to go, forward, left or right?')
        print(f'you moved {direction}')
        return(random.choice(y))


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
    x.direction()
    x.direction()
    x.direction()
    x.direction()
    x.direction()
    print('you move left and move into your kitchen! you succesfully acquire a glass of water and turn to go back to bed.')
    x.direction()
    x.direction()
    x.direction()
    x.direction()
    x.direction()
    x.direction()
    x.direction()
    x.direction()
    print('you move forward and approach the staircase. carefully you walk up stairs, so you dont trip and fall')
    x.direction()
    x.direction()
    x.direction()
    print('you take a sip of water, set it aside and then go back to sleep')
if a == 'no':
    print('goodbye')