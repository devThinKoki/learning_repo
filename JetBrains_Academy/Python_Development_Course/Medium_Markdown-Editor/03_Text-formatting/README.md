## ***Needed Skills***
- Intro to computational thinking
- Components of computational thinking
- Quotes and multi-line strings
- String formatting
- Indexes
- Scopes
- Arguments
- Operations with list
- Functional decomposition

# Goal
Write the code to implement basic markdown in-line tags.

# Description
Congratulations!
You've made it to the most interesting part of the project.
Now we will try to implement the formatters that we have discussed before.
For your convenience, I will copypaste them from the previous stage:
- plain
- **bold**/*italic*
- `inline-code`
- [link](#)
- ###### header
- new-line

We do not include ordered and unordered lists, for now.
This also means that you should delete them from the list shown when a user asks for the `!help` function.
But we will get to them in the next stage!

# Objectives  
Implement a separate function for each of the formatters.
It will keep your code structured.
With functions, you also will be able to find and fix a bug with ease if something is wrong.

The program should work in the following way:
1. Ask a user to input a formatter.
2. If the formatter doesn't exist, print the following error message: `Unknown formatting type or command`
3. Ask a user to input a text that will be applied to the formatter: `Text: <user's input>`.
4. Save the text with the chosen formatter applied to it and print the markdown.
Each time you should print out the whole text in markdown accumulated so far.

Different formatters may require different inputs.

The new-line formatter does not require text input.

Plain, bold, italic, and inline-code formatters require only text input, and should not **add** an extra space or line break at the end:
```
Text: > Some text
```

Headers require a level and text.
A level is a number from 1 to 6.
Don't forget to check it too: if it is out of bounds, print the corresponding error: `The level should be within the range of 1 to 6`.
Also, remember that a heading automatically adds a new line in the end.
```	
Level: > 4
Text: > Hello World!
```

Link requires a label and a URL:
```
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
```

# Example
The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

### **Example 1**:
```
Choose a formatter: > non-existing-formatter
Unknown formatter type or command
Choose a formatter: > header
Level: > 4
Text: > Hello World!
#### Hello World!

Choose a formatter: > plain
Text: > Some plain text
#### Hello World!
Some plain text
Choose a formatter: > new-line
#### Hello World!
Some plain text

Choose a formatter: > link
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
#### Hello World!
Some plain text
[Tutorial](https://www.markdownguide.org/basic-syntax/)
Choose a formatter: > !done
```