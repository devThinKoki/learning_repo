## ***Need Skills***
- Dictionary
- Invoking a function
- Declaring a function
- Arguments
- Basic string methods
- Dictionary methods
- Binary numbers

# Goal
- Write a module that will form a “user profile” based on the data collected in the previous stage.

# Description
- Now it's time to reveal the secret of our magical predictive system.<br>
We will create a "profile" of the user that will contain information about patterns found in their "random" clicks.<br>
To do this, we will count how many times a certain character (0 or 1) follows a specific triad of numbers (for example, 000 or 011).<br>
For example, in the string "00010000", the triad "000" is followed once by a "0" and once by "1".

- In the next stage, we will create a prediction algorithm based on this information.

# Objective
- In this stage, your program should:<br>
    1. Read the user input the same way it did in the previous stage.
    2. Output the result in the following format:<br>
        - `triad`: `counts of 0, counts of 1`, for example, `000: 57,12`.<br>
    - The result for each triad should be printed on a new line.<br>
    The triads must be ordered in ascending order of their decimal representation (for example, 110 in binary = (1* 4) + (1 * 2) + (0 * 1) = 6 in decimal).

# Example
- The greater-than symbol followed by a space (> ) represents the user input.<br>
Note that it's not part of the output.

```
Print a random string containing 0 or 1:

> 01010010010001010100100101001001
The current data length is 32, 68 symbols left
Print a random string containing 0 or 1:

> 10100011001010101010111101001001011010
The current data length is 70, 30 symbols left
Print a random string containing 0 or 1:

> 0101101010100110101010101010001110011

Final data string:
01010010010001010100100101001001101000110010101010101111010010010110100101101010100110101010101010001110011

000: 0,3
001: 10,5
010: 13,18
011: 5,2
100: 3,12
101: 20,3
110: 2,5
111: 2,1
```