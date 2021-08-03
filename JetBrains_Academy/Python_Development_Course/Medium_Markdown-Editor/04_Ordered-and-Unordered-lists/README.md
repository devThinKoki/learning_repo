## ***Needed Skills***
- Computer programming
- Introduction to OOP
- ***Immutability***
- ***Identity testing***
- While loop
- For loop
- **Lambda functions**
- List comprehension
- ***Objects in Python***
- ***Default arguments***
- ***Map and filter***

# Goal
The lists are great! Let's figure out how to use them in our markdown tool.

# Description
There is one more feature that can be very useful!
Imagine going to a grocery store, I bet you would need some kind of a list there
 Markdown lists are straightforward; there are two kinds of them: ordered and unordered.
 I think you've already guessed that the difference between them is that an ordered list itemizes the elements (1., 2., 3., and so on) while an unordered list doesn't do it.

Remember the ordered-list and unordered-list formatters we skipped in the last stage?
Let's get back to them!

# Objectives  
Implement the ordered-list and unordered-list formatters.
You may want to separate the implementation into two different functions, but I suggest keeping them in one; try to get an idea of how to do it!

Both of the formatters require the following input:	
```
Number of rows: > 3
Row #1: > First element
Row #2: > Second element
Row #3: > Third element
```

Don't forget to check that the number of rows is greater than zero!
Otherwise, print the following message: `The number of rows should be greater than zero`

Don't forget about the formatters that we have implemented in the previous stages.

# Examples
The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

### **Example 1**: the formatters automatically add a line break
```
python markdown-editor.py
Choose a formatter: > ordered-list
Number of rows: > 3
Row #1: > First element
Row #2: > Second element
Row #3: > Third element
1. First element
2. Second element
3. Third element

Choose a formatter: > unordered-list
Number of rows: > 2
Row #1: > Fourth element
Row #2: > Fifth element
1. First element
2. Second element
3. Third element
* Fourth element
* Fifth element

Choose a formatter: > unordered-list
Number of rows: > -2
The number of rows should be greater than zero
Number of rows: > 2
Row #1: > Sixth element
Row #2: > Seventh element
1. First element
2. Second element
3. Third element
* Fourth element
* Fifth element
* Sixth element
* Seventh element

Choose a formatter: > !done

```