# Where to Sit Problem

This code simulates a game where n number of people sit around a table. The person at seat 0 starts the game as marked and flips a coin. If it is head gives the ball to the right and gets that person marked as well, if it tails ball goes left. The game continues until everyone except 1 player is marked. The question is where you should sit to have best probability to win?

## Requirements

Python 3.7 or later.
Matplotlib module for data visualization.

## How to Run

Open the terminal.
Navigate to the directory where the code file where_to_sit.py is located.
Type python where_to_sit.py and press enter to run the code.

## Explanation

The program contains two functions: main() and game().

The main() function is responsible for running the simulation multiple times and printing the results. It calls the game() function for each iteration of the game and keeps track of the number of wins for each player.

The game() function simulates one game of the "Where to Sit" problem. It initializes the starting position, marked set, and plays the game until everyone except one player is marked. After each game, it keeps track of the winner and updates the dictionary winners with the number of times the player has won.

Finally, the visualize() function is used to create a scatter plot to visualize the number of wins for each player. It creates two lists x and y from the winners dictionary and plots them using the scatter() function from the Matplotlib module.

## Output

The output of the program is a scatter plot that shows the number of wins for each player. The x-axis represents the seat number, and the y-axis represents the number of wins. The plot can help us identify the best seat to win the game.

## Conclusion

The "Where to Sit" problem is an interesting probability problem that demonstrates how small changes can have a significant impact on the outcome of the game. By simulating the game multiple times, we can identify the best seat to win the game. I haven't shared my findings for not spoiling it. Make sure you have a guess before you run the script.