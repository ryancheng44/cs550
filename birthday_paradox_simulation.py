'''
Ryan Cheng
1/19/2024
Sources: https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list (line 33)
Reflection:

This assignment wasn't too difficult.
The one challenging thing was determining if a list has duplicates.
I found a StackOverflow post that helped me with that.
Everything else was pretty straightforward.

On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

'''
25%: 15 people
50%: 23 people
75%: 32 people
'''

import random

max_num_people = 50
num_trials = 10000

for i in range(max_num_people):
    num_successes = 0
    for _ in range(num_trials):
        birthdays = []
        for _ in range(i):
            birthdays.append(random.randint(1, 365))
        # set() removes duplicates, so if the length of the list is not equal to the length of the set, there are duplicates
        if len(birthdays) != len(set(birthdays)):
            num_successes += 1
    print(f"{i}: {num_successes / num_trials}")