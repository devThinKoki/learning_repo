## ***Needed Skills***
- Quotes and multi-line strings
- Escape sequences
- Type casting
- Invoking a function
- Declaring a function
- [Scopes](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Scopes.md)
- Basic string methods
- [Split and join](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Split-and-join.md)

# Goal
Tic-tac-toe is not all about analysis – a game is meant to be played!<br>
Write a program that can change the state of the field, as your first real step toward a fully-functioning game application!

# Description
It’s time to make our game interactive!<br>
Now we’re going to add the ability for a user to make a move.

To do this, we need to divide the grid into cells.

Suppose the top left cell has the coordinates (1, 1) and the bottom right cell has the coordinates (3, 3) like in this table:
```
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
```

The program should ask the user to enter the coordinates of the cell where they want to make a move.

In this stage, the user plays as X, not O.<br>
Keep in mind that the first coordinate goes from left to right and the second coordinate goes from top to bottom.<br>
Also note that coordinates start with 1 and can be 1, 2, or 3.

What happens if the user enters incorrect coordinates?<br>
The user could enter symbols instead of numbers, or enter coordinates representing occupied cells or cells that aren’t even on the grid.<br>
You need to check the user's input and catch possible exceptions.

# Objectives 
The program should work as follows:
1. Get the 3x3 grid from the input as in the previous stages.
2. Output this 3x3 grid as in the previous stages.
3. Prompt the user to make a move.
4. The user should input 2 numbers that represent the cell where they want to place their X.<br>
(the 9 symbols representing the field will be the first line of input, and the 2 coordinate numbers will be the second line of input)
5. Analyze user input and show messages in the following situations:
`This cell is occupied! Choose another one!` if the cell is not empty.<br>
`You should enter numbers!` if the user enters non-numeric symbols in the coordinates input.<br>
`Coordinates should be from 1 to 3!` if the user enters coordinates outside the game grid.
6. Update the grid to include the user's move and print the updated grid to the console.

The program should also check the user’s input.<br>
If the input is unsuitable, the program should tell the user why their input was wrong, and prompt them to enter coordinates again.

To summarize, you need to output the game grid based on the first line of input, and then ask the user to enter a move.<br>
Keep asking until the user enters coordinates that represent an empty cell on the grid, update the grid to include that move, and then output it to the console.<br>
You should output the field only 2 times: once before the user’s move, and once after the user has entered a legal move.

Do not delete the code you already wrote that analyzes the game state; you will need it in the final step of this project.

The project was changed.<br>
Now the coordinates start from the upper left corner.<br>
Look closely at the examples.

# Example
The examples below show how your program should work.

Notice that after `Enter cells:` and `Enter the coordinates:` comes the user input.

### **Example 1**:
```
Enter cells: X_X_O____
---------
| X   X |
|   O   |
|       |
---------
Enter the coordinates: 3 1
---------
| X   X |
|   O   |
| X     |
---------
```

### **Example 2**:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

### **Example 3**:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 3 3
---------
|   X X |
| O O   |
| O X X |
---------
```

### **Example 4**:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 2 3
---------
|   X X |
| O O X |
| O X   |
---------
```

### **Example 5**:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 3 1
This cell is occupied! Choose another one!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

### **Example 6**:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: one
You should enter numbers!
Enter the coordinates: one one
You should enter numbers!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

### **Example 7**:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 4 1
Coordinates should be from 1 to 3!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```