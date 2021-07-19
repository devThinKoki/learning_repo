## ***Need Skills***
- 

# Goal
- Create a predictor that will guess the user's next input based on their previous keypresses.<br>
We will also validate the performance of this predictor.

# Description
- Now we will start predicting the future user input.<br>
You will be surprised how often people repeat the same patterns!

- Imagine the following:<br>
    - after the second stage for a string `0101010100101001010101000111101010010101010010101010101` we have calculated the amount of a certain character (0 or 1) that follows a specific triad of numbers:<br>
        - `'000': [0, 1]`, `'001': [4, 1]`, `'010': [5, 16]`, `'011': [0, 1]`, `'100': [1, 4]`, `'101': [16, 0]`, `'110': [0, 1]`, `'111': [1, 1]`.<br>
    - Now, the user enters the sequence 001101.<br>
    How can we foresee the next numbers?

- Starting with the 4th character, we can predict the input based on the triads obtained in the previous stage.<br>
We've learned that the combination "001" (the first three characters) was followed by a "0" in 4 cases out of 5.<br>
So, the estimated probability that the user will enter "0" as the fourth character is 4/5 = 80%.<br>
For "1" probability is 1/5 = 20%. Therefore, we will choose "0'" as the fourth character.<br>
Similarly, the 5th character is predicted based on the statistics for the triad preceding it ("011"), and so on.

- And what about the first three characters?<br>
For this task, you don't need to do this.<br>
Generate a sequence of three binary numbers, and that's it.<br>
Based on this triple, make predictions for further symbols.

# Objective
- In this stage, your program should:
    1. Take and preprocess user input as described in stage 1.
    1. Calculate user statistics using triads as described in stage 2 (but don't output the statistics this time).
    1. Ask the user to enter another test string of 0's and 1's the values in which we will try to predict, and preprocess the new input.
    1. Going through the string entered by the user, estimate the frequency of occurrence of "0" or "1" after each triad and generate predictions:<br>
        - if the count of 0's after the current triad is higher, the program should predict "0", otherwise, predict "1".<br>
        - If the counts are equal, the choice can be made in a random way.
    1. The first three symbols may be predicted by chance one by one using the `random` module.<br>
    You can also invent your own algorithm here, for instance, make use of the overall frequencies of 0's and 1's in the user input.
    1. Test the accuracy of our predictor (excluding the first 3 randomly predicted symbols) by comparing the real input and the prediction.<br>
    As the final output, print the line `Computer guessed right N out of M symbols (ACC%)`, where `N` is the number of correctly guessed symbols, `M` is the total length of the test input, and `ACC` is the accuracy value with 0.01% precision.<br>
    Remember to exclude the first 3 symbols from the calculation!

# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

```
Print a random string containing 0 or 1:

> 0101001010010101011111100010010110000101010101010100101
The current data length is 63, 37 symbols left
Print a random string containing 0 or 1:

> 01010101001010010101010001111001010010101010010101010101

Final data string:
010100101001010101111110001001011000010101010101010010101010101001010010101010001111001010010101010010101010101


Please enter a test string containing 0 or 1:

0110001010100101
prediction:
1101011010101101

Computer guessed right 10 out of 13 symbols (76.92 %)
```
