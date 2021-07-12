## ***Need Skills***
- Set
- For loop

# Goal
- Using a loop, extend the number of attempts to eight.
- Now we're talking!

# Description
- Let's make the game iterative.
<br>Now it's time to make the game resemble the classic version of Hangman a bit more.
<br>The player should now guess letters in the word instead of typing the entire word all at once.
<br>If the player guesses a letter, it should be uncovered in the word.
<br>For now, start by building the defeat condition and add 8 tries to guess a letter that appears in the word.
<br>When the player runs out of attempts, the game ends.
<br>
<br>Later we will determine the winning conditions, but in this stage, let's just see how well our player guesses the word on each attempt.

# Objective
- Now your game should work as follows:
    1. A player has exactly 8 tries and enters letters.
    <br>Nothing changes if a player has more tries left but they have already guessed the word.
    2. If the letter doesn't appear in the word, the computer takes one try away – even if the user has already guessed this letter.
    3. If the player doesn't have any more attempts, the game should end and the program should show a losing message.
    <br>Otherwise, the player can continue to input letters.
    4. Also, the word should be selected from our list:
    <br>&nbsp;&nbsp;&nbsp;&nbsp;'python', 'java', 'kotlin', 'javascript',
    <br>so that your program can be tested more reliably.
    ```
    Please, make sure that your program's output formatting precisely follows the example.
    Pay attention to the empty lines between tries and at the end.
    ```
    
# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

- Example 1
```
H A N G M A N

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word

-a-a---i--
Input a letter: > z
That letter doesn't appear in the word

-a-a---i--
Input a letter: > l
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > p

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word

Thanks for playing!
We'll see how well you did in the next stage
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
Input a letter: > o
That letter doesn't appear in the word

j---
Input a letter: > a

ja-a
Input a letter: > v

java
Input a letter: > a

java
Input a letter: > j

Thanks for playing!
We'll see how well you did in the next stage
```
