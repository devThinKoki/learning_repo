## ***Needed Skills***
- [Introduction to Python](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Introduction-to-Python.md)
- [Overview of the basic program](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Overview-of-the-basic-program.md)
- [Multi-line programs](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Multi-line-programs.md)
- [PEP 8](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/PEP-8.md)
- [Comments](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Comments.md)
- [Basic data types](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Basic-data-types.md)
- [Integer arithmetic](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Integer-arithmetic.md)
- [Variables](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Variables.md)
- [Naming variables](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Naming-variables.md)
- [Taking input](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Taking-input.md)
- [Program with numbers](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Program-with-numbers.md)
- [Boolean logic](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Boolean-logic.md)
- [Comparisons](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Comparisons.md)
- [If statement](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/If-statement.md)
- [Else statement](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Else-statement.md)
- [Elif statement](https://github.com/devThinKoki/learning_repo/tree/main/JetBrains_Academy/Theories/Elif-statement.md)

# Goal
Before learning how to play the game properly, let’s learn how to cheat!<br>
Using conditional statements, you’ll write a program that always defeats the human player in the Rock-Paper-Scissors game.

# Description
Rock, paper, scissors is a well-known hand game.<br>
Each one of two players simultaneously forms one of three shapes with their hands, and then, depending on the chosen shapes, the winner is determined: rock beats scissors, paper wins over rock, scissors beat paper.<br>
The game is widely used to make a fair decision between equal options.

So, let's start with an unfair version! :)

Write a program that reads input specifying which option the user has chosen.<br>
Then your program should make the user lose!<br>
That is, your program should always choose an option that defeats the one picked by the user.<br>
After finding this option, output a line `Sorry, but the computer chose <option>`, where `<option>` is the name of option that the program picked depending on the user's input.<br>
For example, if the user enters `rock`, the program should print `Sorry, but the computer chose paper` and so on.

Please, pay attention to the format of the output.<br>
It should be exactly the same as in the example, including capital letters and punctuation.<br>
No additional strings should be printed!

# Objectives 
Your program should:
1. Take an input from the user
2. Find an option that wins over the user's option
3. Output a line: `Sorry, but the computer chose <option>`

# Example
The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

### **Example 1**
```
> scissors
Sorry, but the computer chose rock
```

### **Example 2**
```
> paper
Sorry, but the computer chose scissors
```