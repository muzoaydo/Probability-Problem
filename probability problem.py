import matplotlib.pyplot as plt
from random import choice


range = 100
start_pos = 0
winners = {}
iterations = 1000


def main():
    for i in range(iterations):
        game()
    # winners = sorted(winners)
    print(winners)
    visualize(winners)

def game():

    marked = set()
    cur_pos = start_pos

    # Keep going until all players are marked.
    while len(marked) != range - 1:

        # Mark the first person 
        marked.add(cur_pos)

        # Flip the coin
        coin = choice(["Head", "Tails"])

        # If 'Head' give the ball to your right. If 'Tails' give left instead.
        if(coin == "Head"):
            cur_pos += 1
        else:
            cur_pos -= 1

    # Last person who has the ball is winner.    
    print(f"Winner is {cur_pos}")
    # Keep track of the wins.
    cur_val = winners.get(cur_pos)
    if cur_val is None:
        cur_val = 0

    winners[cur_pos] = cur_val + 1

# Using matplotlib to get a scattered graph of winners.
def visualize(winners):

    # Create x and y lists from dictionary
    x = list(winners.keys())
    y = list(winners.values())

    # Create scatter plot
    plt.scatter(x, y, s=10)

    # Set plot title and axis labels
    plt.title("Where to sit problem.")
    plt.xlabel("Seats")
    plt.ylabel("Wins")

    # Show plot
    plt.show()

main()


