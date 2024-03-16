'''
Ryan Cheng
1/29/2024
Sources: https://w.wiki/8ysy (General information about the St. Petersburg Paradox)
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

import random
import matplotlib.pyplot as plt

num_trials = 1000000
results = []

for _ in range(num_trials):
    num_consec_tails = 0

    # flip a coin until it lands on heads
    while random.randint(0, 1) == 0:
        num_consec_tails += 1

    # append the log2 of the winnings to the results list
    # winnings = 2 ** (num_consec_tails + 1)
    results.append(num_consec_tails+1)

# bins=range(min(results), max(results)+1) makes the bins go from 1 to the max value in the results list
# density=True makes the y-axis the proportion of trials instead of the number of trials
plt.hist(results, bins=range(min(results), max(results)+1), edgecolor='black', density=True)
# use log scale because the proportions get extremely small
plt.yscale('log')

# add labels and title
plt.xlabel('Log2 of Winnings')
plt.ylabel('Proportion of Trials')
plt.title(f'Results of {num_trials} Trials of the St. Petersburg Paradox')

plt.show()