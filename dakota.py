'''
Ryan Cheng
9/11/23
Sources: None
Reflection: I don't have much to say, but it was fun coming up with silly questions and goofy responses. :)
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

print("Hello! My name is Copilot.")

name = input("What's your name? ").strip()
print("Hello " + name + "!")

location = input("Where are you from? ").lower().strip()
if location == "pennsylvania" or location == "pa":
    print("I'm from Pennsylvania too!")
else:
    print("That's cool! I'm from Pennsylvania.")

flavor = input("What's your favorite ice cream flavor? ").lower().strip()
if flavor == "black raspberry":
    print("That's awesome, me too!")
else:
    print("Ewww! You're disgusting. I don't know if I want to continue talking to you.")

genius = input("Who's your favorite genius? ").lower().strip()
if genius == "oppenheimer":
    print("That's crazy! I'm actually Oppenheimer; it's nice to meet you!")
else:
    print("That's cool because I'm Oppenheimer;\nI've actually collaborated with them before.")

tyre = input("What's your favorite tyre brand? ").lower().strip()
if tyre == "pirelli":
    print("They're trash. I can't believe F1 uses them.")
else:
    print("Fire choice. F1 should switch to them. I'm also sponsored by them;\nI use them on my Bugatti Chiron.")

color = input("What color's your Bugatti? ")
print("I don't care. I'm going to go play some video games. Bye!")