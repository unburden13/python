import sys
from random import randint

#  param values coming from terminal
#  call example: C:\Git\python\modules> python guessing_game.py 3 13

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    number_to_guess = randint(start, end)

    while True:
        try:
            guess = int(input(f'enter a guess between {start} ~ {end}: '))

            if start <= guess <= end:  # suggestion by the IDE, before: if guess >= start and guess =< end:
                if guess == number_to_guess:
                    print('mostro!')
                    break
                else:
                    print('keep trying')
            else:
                print(f'hey, are you mad? I said {start} ~ {end}')
        except ValueError:
            print('Please enter a number')

except ValueError as err:
    print('Please enter numbers in the range')


