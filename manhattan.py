'''
Ryan Cheng
9/23/23
Sources:
    How to use quotation marks in strings (line 35):
    https://note.nkmk.me/en/python-str-literal-constructor/#:~:text=source%3A%20str_literal.py-,Quotes%20in%20strings%20are%20handled%20differently,is%20also%20permissible%2C%20but%20unnecessary.

    Check if a string is a letter (line 58):
    https://www.w3schools.com/python/ref_string_isalpha.asp

    Check if a string is present in another string (line 85):
    https://www.digitalocean.com/community/tutorials/python-find-string-in-list#

    How to append to a list (line 90):
    https://www.w3schools.com/python/ref_list_append.asp

    How to substring a string (line 98):
    https://www.w3schools.com/python/ref_string_slice.asp

Reflection: It was challenging but fun to come up with an idea for a program that would meet all the rubric requirements.
            When I decided on a guessing game, I knew that I would make two functions for getting a letter input:
            One for getting plain old string input with try and except, and another that used the aforementioned function
            to get a string input and check if it was one singular letter. However, I tried to code the entire game without
            splitting it up into functions, and I ended up with hard to read code. I then decided to split the code
            into two functions. I enjoyed learning a bit more about python syntax... I'm warming up to it as there are so
            many shorthand notations, but I still dislike how types are not explicitly defined and that there are no curly
            brackets; I have no idea where my functions end!!!
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

import random

def welcome():
    # quotation marks in strings (external source)
    print("Welcome to \"Guess the Phrase\"!")
    print("In this game, you will have to guess a phrase.")
    print("You will take turns guessing a letter in the phrase.")
    print("If you guess a letter that is in the phrase, you will be shown where the letter is in the phrase.")
    print("If you guess a letter that is not in the phrase, you will lose a life.")
    # formatted string
    print(f"You will have {lives} lives.")

def get_input(prompt):
    # ensures valid input
    while True:
        try:
            return input(prompt).lower().strip()
        except ValueError:
            print("You entered an invalid input. Please, try again.")

def get_letter(prompt):
    # ensures input of a single letter, other cases are handled by notifying the user what they did wrong
    while True:
        letter = get_input(prompt)
        if letter == "":
            print("You did not enter anything. Please, try again.")
        # ensures input is an alphabetic letter and not a symbol or number (external source)
        elif not letter.isalpha():
            print("You entered a non-letter. Please, try again.")
        elif len(letter) > 1:
            print("You entered more than one letter. Please, try again.")
        else:
            return letter

def play_game():
    # grab lives from global scope
    global lives
    random_phrase = random.choice(phrases)
    guessed_letters = []
    guessed_phrase = ""
    # turns the phrase into a string of underscores and spaces; for instance, "happy birthday" would become "_____ ________"
    for c in random_phrase:
        if c == ' ':
            guessed_phrase += ' '
        else:
            guessed_phrase += '_'
    
    print(f"I have chosen a phrase. Here is what the phrase looks like: {guessed_phrase}")

    while lives > 0:
        print(f"You have {lives} lives remaining.")
        letter = get_letter("Please, enter a letter: ")

        # if the letter was already guessed, do nothing and skip to the next iteration of the loop (external source)
        if letter in guessed_letters:
            print("You have already entered this letter. Please, try again.")
            continue

        # add the letter to the list of guessed letters (external source)
        guessed_letters.append(letter)
        
        if letter in random_phrase:
            # replace the underscores in the guessed phrase with the guessed letter where they appear in the random phrase
            for c in range(len(random_phrase)):
                if random_phrase[c] == letter:
                    # grab the substring of the guessed phrase before the letter, add the letter,
                    # and then add the substring of the guessed phrase after the letter (external source)
                    guessed_phrase = guessed_phrase[:c] + letter + guessed_phrase[c+1:]

            # if the guessed phrase is the same as the random phrase, the user has won
            if guessed_phrase == random_phrase:
                print(f"You got it! The phrase is \"{random_phrase}\".")
                return
            
            print(f"Yes! The letter '{letter}' is in the phrase.")
        else:
            print(f"Sorry, the letter {letter} is not in the phrase.")
            lives -= 1

        print(f"Here is what you have so far: {guessed_phrase}")

    print(f"Sorry, you lost. The phrase was \"{random_phrase}\".")

# end of functions, start of main (runtime code)

phrases = ["go choate", "i dislike python", "lose yourself", "kohler environmental center", "life is really simple but we insist on making it complicated"]
lives = 10

welcome()

# infinite loop until the user enters either "y" or "n"
while True:
    answer = get_letter("Do you want to play? (y/n) ")
    if answer == "y":
        print("Great, let's play!")
        break
    elif answer == "n":
        print("That's alright. Come back another time; goodbye!")
        exit()
    else:
        print("Please enter either 'y' or 'n'")

play_game()

'''
Leon Gopaul - I really like your code and the idea of a guessing game. However, I think you should add a few comments in your code so that it is easily understandable.
Response: Thank you for your feedback. I added some comments to my code.

Ryan Chapman - I really like the hangman game, however, sometimes it can be confusing, maybe if you come back to the game you can tell the user if they've already used a letter if they accidentaly type it in again.
Response: Thank you for your feedback. I added a check to see if the user has already guessed a letter.
'''