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
        direction2 = input('which way do you want to go, forward left or right?')
        if direction2 == 'left':
            print('you encounter a monster!')
            direction2 = input('forward left or right?')
        if direction2 == 'right':
            print('you bump into a wall. ouch!')
            direction2 = input('forward left or right?')
        if direction2 == 'forward':
            print('you move forward.')
            direction3 = input('which way do you want to go, forward left or right?')
            if direction3 == 'left': 
                print('you move left. but thats the bathroom. try going a different direction')
                direction3 = ('forward left or right?')
            if direction3 == 'forward':
                print('you move forward and bump into a wall. ouch! try going a different direction')
                direction3 = ('forward left or right?')
            if direction3 == 'right':
                print('you move forward and approach the staircase. carefully you walk down stairs, so you dont trip and fall')
                direction4 = input('which way do you want to go, forward left or right?')
                if direction4 == 'left':
                    print('you move left and encounter a monster')
                    direction4 = input('forward left or right?')
                if direction4 == 'forward':
                    print('you move forward and encounter a monster') 
                    direction4 = input('forward left or right') 
                if direction4 == 'right':
                    print('you move right')   
                    direction5 = input('which way do you want to go, foward left or right?')
                    if direction5 == 'forward':
                        print('you move forward and encounter a monster')
                        direction5 = input('forward ')
                    if direction5 == 'left':
                        print('you move left and encounter a monster')
                        direction5 = input('forward left or right?')
                    if direction5 == 'right':
                        print('you move right')
                        direction6 = input('which way do you want to go, forward left or right?')
                        if direction6 == 'left':
                            print('you move left and you bump into a wall. ouch! try going in a different direction')
                            direction6 = input('forward left or right?')
                        if direction6 == 'right':
                            print('you move right and bump into a wall. ouch! try going in a different direction')
                            direction6 = input('forward left or right?')
                        if direction6 == 'forward':
                            print('you move forward')
if x == 'no':
    print('goodbye')