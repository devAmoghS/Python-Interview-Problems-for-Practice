"""
David vs. Goliath Gambler's Ruin Simulation

This program simulates a gambling scenario between two players: David and Goliath.
David has a skill advantage, represented by a 55% probability of winning each round,
while Goliath has a size advantage with a larger initial amount of money.

Assumptions:
- David starts with $2,000, and Goliath starts with $10,000.
- Each round of betting results in a transfer of $1,000 from the loser to the winner.
- The game continues until one player runs out of money (i.e., their amount reaches zero).
- The outcome of each round is determined by a random number generator, reflecting David's skill advantage.

Mathematics:
- The simulation models a stochastic process where each round can be viewed as an independent Bernoulli trial:
  - David wins with a probability of 0.55.
  - Goliath wins with a probability of 0.45.
- The expected outcomes can be analyzed using concepts from probability theory and stochastic processes.
- The simulation runs for a specified number of trials to gather statistical data on how often David wins compared to Goliath.

Usage:
1. Run the program in a Python environment.
2. Input the desired number of simulations when prompted.
3. The program will output the number of wins for both David and Goliath and display a bar chart of the results.

This simulation provides insights into how skill can offset size advantages in competitive scenarios.
"""

import random
import matplotlib.pyplot as plt

def gambler_ruin(david_initial, goliath_initial, david_win_prob, simulations):
    results = []
    
    for _ in range(simulations):
        david_amount = david_initial
        goliath_amount = goliath_initial
        
        while david_amount > 0 and goliath_amount > 0:
            # Simulate a single bet based on David's winning probability
            if random.random() < david_win_prob:  # David wins
                david_amount += 1000
                goliath_amount -= 1000
            else:  # Goliath wins
                david_amount -= 1000
                goliath_amount += 1000
        
        # Record the result: True if David wins, False if Goliath wins
        results.append(david_amount > 0)
    
    return results

def plot_results(results):
    wins = sum(results)
    losses = len(results) - wins
    
    plt.bar(['David Wins', 'Goliath Wins'], [wins, losses], color=['blue', 'red'])
    plt.title('David vs. Goliath Simulation Results')
    plt.ylabel('Number of Simulations')
    plt.show()

def main():
    david_initial = 2000  # David's initial amount
    goliath_initial = 10000  # Goliath's initial amount
    david_win_prob = 0.51  # David's skill advantage (55%)
    simulations = int(input("Enter number of simulations: "))

    results = gambler_ruin(david_initial, goliath_initial, david_win_prob, simulations)
    
    print(f"\nResults after {simulations} simulations:")
    print(f"David Wins: {sum(results)}")
    print(f"Goliath Wins: {len(results) - sum(results)}")
    
    plot_results(results)

if __name__ == "__main__":
    main()
