secret_word = "conundrum"
max_guesses = 3
guess_count = 0
guess = ""
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < max_guesses:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
else:
    print("Finish guesses check")  # does not get executed in case a break is reached inside the loop

if out_of_guesses is False:
    print("You win")
else:
    print("Out of guesses, you lose!")
