from random import randint

start = 1
end = 10


def check_guess(guess_value, answer):
    if start <= guess_value <= end:  # suggestion by the IDE, before: if guess >= start and guess =< end:
        if guess_value == answer:
            print('mostro!')
            return True
        else:
            print('keep trying')
            return False
    else:
        print('guess is not inside the range')
        return False


if __name__ == '__main__':  # this is so the test file does not run the program
    try:
        number_to_guess = randint(start, end)

        while True:
            try:
                guess = int(input(f'enter a guess between {start} ~ {end}: '))
                if check_guess(guess, number_to_guess):
                    break
            except ValueError:
                print('Please enter a number')

    except ValueError as err:
        print('Please enter numbers in the range')


