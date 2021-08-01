## ***Needed Skills***
- Multi-line programs
- PEP 8
- Comments
- Basic data types
- Integer arithmetic
- Variables
- Naming variables
- Taking input
- Program with numbers
- List
- Boolean logic
- Comparisons
- Invoking a function
- Declaring a function
- If statement
- Else statement
- Elif statement
- ***Markdown: extended elements***

# Goal
Think about the functionality and code a piece to help users understand how the tool works.

# Description
Before we start implementing the project, we need to think about the functionality.
Remember [the Markdown Guide](https://www.markdownguide.org/basic-syntax/) from the previous stage?
Let's go through it one more time and recall the basic features:
* plain — a normal text without any formatting
* bold/italic — self-explanatory
* inline-code — for example, `python editor.py`
* link — for example, [google.com](https://www.google.com/)
* header — look at the header of this stage.
* unordered-list — this very list is an example of an unordered list
* ordered-list — a list with enumerated elements
* new-line — switches to the next line

In this stage, you need to implement these features in your editor.
Let's also add special commands to our tool:
* !help — prints available syntax commands.
* !done — saves the markdown and exits the app.

Let's do it!

# Objectives  
Implement the help function that will print available syntax commands, which we have indicated above, as well as the special commands.
When called, it should print the following:
```
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
```

Implement the exit function that exits the editor without saving.

Ask a user for input:
```
Choose a formatter:
```
`!help` prints the help page, `!done` exits the editor.

If the input contains one of the correct formatters (plain, bold, italic, etc.), ask for the input once again.

If the input contains no formatters or unknown command is sent, print the following message and ask for input again: `Unknown formatting type or command`

# Example
The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

### **Example 1**:
```
Choose a formatter: > non-existing-formatter
Unknown formatting type or command
Choose a formatter: > !help
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
Choose a formatter: > header
Choose a formatter: > ordered-list
Choose a formatter: > !done
```