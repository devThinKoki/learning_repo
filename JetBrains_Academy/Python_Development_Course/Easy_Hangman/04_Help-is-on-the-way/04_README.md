## ***Need Skills***
- Quotes and multi-line strings
- String formatting
- ***Basic string methods
- ***Search in a string
- IDE
- PyCharm basics

# Goal
- Enable hints in your game. 
- Allow it to show the number of letters and the first three letters. 
- Slicing will help you to implement this part.

# Description
- Now our game has become quite hard, and your chances of guessing the word depend on the size of the list. 
- When the list has four words, you only have a 25% chance to guess correctly. 
- So let's show a little mercy to the player and add a hint for them.

# Objectives
1. As in the previous stage, you should use the following word list:<br>
&nbsp;&nbsp;&nbsp;&nbsp;'python', 'java', 'kotlin', 'javascript'
2. Once the computer has chosen a word from the list, show its first 3 letters.<br> 
Hidden letters should be replaced with hyphens ("-").

# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

- Example 1
```python
H A N G M A N
Guess the word jav-: > java
You survived!
```
- Example 2
```python
H A N G M A N
Guess the word pyt---: > pythia
You lost!
```