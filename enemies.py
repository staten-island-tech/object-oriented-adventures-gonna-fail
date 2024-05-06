x = input("you wake up in the middle of the night, thirsty. do you want to get a glass of water?")


if x == 'yes':
    direction = input('you get out of bed and open your door. forward left or right?')
    if direction == 'left':
        print('you move left. you bump into a wall. ouch! try going the other way')
        direction = input('forward left or right?')
    if direction == 'right': 
        print('you move right. you bump into a wall. ouch! try going the other way')
        direction = input('forward left or right?')
    if direction == 'forward':
        print('you move forward')
        direction2 = input('which way do you want to go, left right or forward?')
        if direction2 == 'left':
            print('you encounter a monster!')
        if direction2 == 'right':
            print('you bump into a wall. ouch!')
        if direction2 == 'forward':
            print('you move forward.')
            direction2 = input