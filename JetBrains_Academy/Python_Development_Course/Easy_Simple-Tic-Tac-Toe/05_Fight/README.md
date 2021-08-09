## ***Needed Skills***
- Program execution
- While loop
- Loop control statements
- Errors
- [Any and all](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Any-and-all.md)

# Goal
Finally!<br>
Thanks to this app, you can always challenge a friend to play a quick game of Tic-Tac-Toe!

# Description
Our game is almost ready!<br>
Now let's combine what we’ve learned in the previous stages to make a game of tic-tac-toe that two players can play from the beginning (with an empty grid) through to the end (until there is a draw, or one of the players wins).

The first player has to play as X and their opponent plays as O.

# Objectives 
In this stage, you should write a program that:
1. Prints an empty grid at the beginning of the game.
2. Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
3. Ends the game when someone wins or there is a draw.

You need to output the final result at the end of the game.

Good luck!

> The project was changed.<br>
> Now the coordinates start from the upper left corner.<br>
> Look closely at the examples.

# Example
The example below shows how your program should work.<br>
Notice that after `Enter the coordinates:` comes the user input.
```python
---------
|       |
|       |
|       |
---------
Enter the coordinates: 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: 2 2
This cell is occupied! Choose another one!
Enter the coordinates: two two
You should enter numbers!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: 3 3
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: 2 1
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: 3 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: 2 3
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
```