'''
Ryan Cheng
9/11/23
Sources: https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/ (Using Else Conditional Statement With For loop in Python, line 36)
Reflection: I really enjoyed the bonus challenge! I learned how to use the else statement with a for loop, something I believe is exclusive to Python?
            I don't remember ever using it in C#.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

import random

# give the user a near infinite amount of guesses the first time
max_number_of_guesses = 1000000
points = 0

while True:
    # generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    print(f"New game! Guess a number between 1 and 10. You have {max_number_of_guesses} guess(es).")

    # give the user a limited amount of guesses
    for guesses in range(max_number_of_guesses):
        guess = int(input("Guess: "))
        if guess == random_number:
            # set the max number of guesses to the current number of guesses (need to add 1 because guesses starts at 0) and add a point
            max_number_of_guesses = guesses + 1
            points += 1
            print(f"You win! You took {guesses + 1} guess(es). You have {points} point(s).")
            break
        elif guess > random_number:
            print("Too high!")
        else:
            print("Too low!")

    # if the user runs out of guesses, tell them the number and end the game
    else:
        print(f"Game over! The number was {random_number}. You took too many guesses.")

    play_again = input("Want to play again? (y/n) ")
    if play_again.lower() != "y":
        break
