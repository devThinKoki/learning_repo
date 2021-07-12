## ***Need Skills***
- Program execution
- Errors

# Goal
- Improve the game by handling different error cases.
<br>Repetition of a letter, entering words that are too long, or using non-Latin characters shouldn’t cost your player a life.

# Description
- Now that we are done with the basics, let's work on perfecting some details.

- In the previous stage, if the user entered the same letter twice, the program reduced the number of remaining attempts regardless of whether this was a correct letter or not.
<br>This doesn’t seem fair to the player, does it?
<br>They gain no additional information about the situation on the field yet the program still reduces their remaining attempts.
<br>Let's fix it!

# Objective
1. If the user enters the same letter twice, then the program should output `You've already guessed this letter`.
<br>This message should also be printed if the user inputs a letter that doesn't appear in the word.
<br>The number of attempts shouldn't be decreased in this case.

1. Also, you should check to make sure the player entered an English lowercase letter.<br>
If not, the program should print `Please enter a lowercase English letter`.

1. You should also check if the player entered exactly one letter.<br>
If not, the program should print `You should input a single letter`. <br>Remember that zero is also not one!

1. Note that none of these three errors should reduce the number of remaining attempts!
```
Please, make sure that your program's output formatting precisely follows the output formatting in the example.
Pay attention to the empty lines between tries and in the end.
```

# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

- Example 1
```
H A N G M A N

------
Input a letter: > t

--t---
Input a letter: > z
That letter doesn't appear in the word

--t---
Input a letter: > t
No improvements

--t---
Input a letter: > t
No improvements

--t---
Input a letter: > y

-yt---
Input a letter: > x
That letter doesn't appear in the word

-yt---
Input a letter: > y
No improvements

-yt---
Input a letter: > p

pyt---
Input a letter: > p
No improvements

pyt---
Input a letter: > q
That letter doesn't appear in the word

pyt---
Input a letter: > p
No improvements
You lost!
```
- Example 2
```
H A N G M A N

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > a

ja-a
Input a letter: > v

java
You guessed the word!
You survived!
```
