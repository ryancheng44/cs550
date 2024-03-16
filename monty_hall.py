'''
Ryan Cheng
1/7/24
Sources: None
Reflection: I think it is better to switch.
            Let's say you always switch.
            If you pick the car and switch, you always lose.
            If you pick a goat and switch, you always win (because the host reveals the other goat).
            The chance of you picking a goat is 2/3 compared to 1/3 for picking a car.
            Let's say you always stay.
            If you pick the car and stay, you always win.
            If you pick a goat and stay, you always lose.
            The chance of you picking a goat is 2/3 compared to 1/3 for picking a car.
            Therefore, it is better to switch.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

import random

def monty_hall(times, switch):
    doors = ['goat', 'goat', 'car']
    times_won = 0
    
    for i in range(times):
        random.shuffle(doors)
        choice = random.randint(0, 2)
        for i in range(3):
            if doors[i] == 'goat' and i != choice:
                reveal = i
                break
        if switch:
            for i in range(3):
                if i != choice and i != reveal:
                    choice = i
                    break
        if doors[choice] == 'car':
            times_won += 1
    return times_won / times

print(monty_hall(10000, False))
print(monty_hall(10000, True))

'''
Staying results in a 1/3 chance of winning.
Switching results in a 2/3 chance of winning.
This is what I expected, although I have encountered this problem before.
It took me a while to understand it.
I found the explanation I wrote above in the comment section of a YouTube video.
That's when I finally understood it.
'''