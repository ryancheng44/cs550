'''
Ryan Cheng
1/9/2024
Sources: Sebastian Plunkett gave me the idea on how to check whether a point is in the circle.
Reflection:

At first, I was kind of confused by the assignment.
I originally used random.random() < 0.25 * math.pi to check whether a point was in the circle, but I realized that this was circular.
I was stuck trying to think of a way to check whether a point was in the circle in a non-circular way when Sebastian suggested that I use the distance formula.
Then the rest of the assignment became extremely easy.

On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

'''
1. State the diameter of the circle, and the radius of the circle. 1, 0.5
2. What is the area of the square? 1
3. What is the area of this circle, in terms of pi? 0.25pi
4. If you were to choose a position within the square randomly, how likely is it that it would be wthin the circle? 0.25pi
'''

import random
import math

def program(trials):
    successes = 0
    for _ in range(trials):
        x = random.random()
        y = random.random()
        if math.sqrt((x - 0.5)**2 + (y - 0.5)**2) < 0.5:
            successes += 1
    return successes / trials * 4

print(program(10))
print(program(100))
print(program(1000))
print(program(10000))
print(program(100000))

'''
6. What number are you close to? pi
7. Think about what we are approximating, and why this works. Explain in a paragraph your conclusions.

We are approximating pi.
Pi is the ratio of a circle's circumference to its diameter.
So, circumference = pi * diameter, or pi * 2 * radius.
From this, we can derive that the area of a circle is pi * radius^2. (See Archimedes' expansion of a circle into infinite slices if necessary.)
Assume a square with side length 1, and a circle with diameter 1. The circle is inscribed in the square such that the circle's center is the same as the square's center.
We know that the area of the square is 1, and the area of the circle is pi * 0.5^2 = 0.25pi.
So the probability of a random point in the square being in the circle is 0.25pi or pi/4.
We can approximate this probability by randomly generating points in the square and seeing how many are in the circle.
We can then multiply this probability by 4 to get an approximation of pi.
(probability = pi/4 --> probability * 4 = pi)
'''