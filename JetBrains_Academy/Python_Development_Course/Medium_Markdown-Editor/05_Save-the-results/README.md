## ***Needed Skills***
- Introduction to operating systme
- **Files**
- File types
- Command line overview
- Introduction to Linux
- File modes and permissions
- Working with file modes and permissions
- Files in Python
- **Reading files**
- **Writing files**

# Goal
Learn how to save your results to a file.

# Description
By this moment, our program can recognize some of the formatters and special commands, it can also print the results and exit.<br>
We need to implement yet another very useful feature - the ability to save the text to a file.

# Objectives 
Modify your `done` function that was implemented in the second stage.<br>
Apart from exiting the program, it should save the final result of a session to a file, let's call it `output.md`.<br>
Create this file in the program directory.<br>
If it already exists, overwrite this file.<br>
The file should include the result of the last session. 

# Example
The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

### **Example 1**:
```
Choose a formatter: > header
Level: > 1
Text: > Hello World!
# Hello World!

Choose a formatter: > plain
Text: > Lorem ipsum dolor sit amet, consectetur adipiscing elit
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
Choose a formatter: > line-break
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit

Choose a formatter: > ordered-list
Number of rows: > 3
Row #1: > dolor
Row #2: > sit
Row #3: > amet
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
1. dolor
2. sit
3. amet

Choose a formatter: > !done
```
# Afterword
