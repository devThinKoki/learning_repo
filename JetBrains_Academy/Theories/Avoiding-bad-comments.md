# Avoiding bad comments
As you already know, a Python feature (beloved by all Python programmers) is its **well-readable syntax**.<br>
However, apart from the syntax itself, there are other important things that contribute to the readability of your program.<br>
We assume that you are already familiar with **comments** and how they help in learning a new language.

In real programs, comments become especially important as the program gets bigger and more complicated.<br>
Without them, things may get confusing even for you within a few months after writing the program, not to mention other developers who see your code for the first time.<br>
However, there is also a downside of making comments, meaning that more is not necessarily better, and we will discuss it below as well.

## 1. When not to write comments?
This may sound strange but sometimes it's better not to write comments at all.<br>
Carefully written, they can indeed contribute to the readability of your program, but it doesn't mean you should include them wherever you can.<br>
On the contrary, many programmers are convinced that a good piece of code doesn't require any comments in the first place, for it is so transparent and accurate.<br>
That is what we all should aim at.<br>
So, if code can be made self-explanatory, comments are unnecessary, and it's better to change the code.<br>
Let's highlight cases when developers need to comment less.
- If a comment explains a **variable/function**, you can usually delete the comment and **explicitly name** the variable/method itself.<br>
Compare the following lines of code:
```python
n = 0  # number of participants
participants_num = 0
```

- Avoid writing ```obvious comments```, like the one below.<br>
They make your code redundant and even harder to read.<br>
You should always seek to follow the D.R.Y. (don't repeat yourself) principle, not W.E.T. ("wrote everything twice" or "wasted everyone's time" for more cynical ones).
```python
age = 20  # age is 20
greeting = 'hello'  # assign 'hello' to greeting
```
- If you see a way to alter your code so that `comments` would become `unnecessary` - you should do that.

That is, if you can avoid commenting — you'd better do.<br>
Then your code would be clean, wouldn't be overloaded with unnecessary details and wouldn't become more complicated rather than clearer for readers to understand.

## 2. How to write good comments?
Now, let's turn to cases when you decide to write a comment.<br>
The main thing to remember then is that comments should be easily **understandable** by anyone, be that Future You or some other programmer.<br>
Here are some tips on how to achieve it:
- Generally, comments should answer the question **"why"** as opposed to **"what"**.<br>
However, it may be **useful for beginners** to write comments for themselves explaining what the code does, especially when using a newly learned syntax expression, e.g.:
```python
result = 15 % 4  # % is used for division with remainder
```

- Make sure that your comments do not **contradict the code** (that happens more often than you can imagine!).<br>
Wrong comments are worse than no comments at all.
```python
# decrease the counter
counter += 1
```

- Do not forget to `update` the comments if you modify the code.<br>
It will only confuse the reader instead of helping them.<br>
In the example below, the variable "counter" used to be designated as "i"; the programmer changed its name in the code but not in the comment.
```python
# i is incremented in case of errors
counter += 1
```

Following these pieces of advice, you can write code that is clean, organized, easy to understand, and pleasant to read.

## 3. Conclusion
When annotating the code, it's important to know where to draw the line.<br>
Both **overcommented-** and **undercommented programs** can be difficult to understand, resulting in wasted and unpleasant time spent working with such pieces of code.<br>
So, you should always try to write comments carefully and only **when necessary**.

The simplest way to learn to do so is just by doing it.<br>
It's a good idea to start practicing when you only start coding because you will get used to it, and by the time some more complex problems should be solved, you will know how to write comments properly.<br>
From now on, try to **include simple comments** in your code to explain difficult moments that took you a while to understand.<br>
It is also useful to get back to **review** your **older programs** and see how they (including comments) could be enhanced.

## 4. Practices
### 1. Improvement Choices
Generally, comments are a great idea, but now it's time to improve some of them.

Match the examples below with the corresponding fixes.

> Answer
```python
a = input() # the first variable from user input is name
>>> # Change the name of the variable

name, surname = "Ned", "Stark" # assigning name to name and surname to surname
>>> # Avoid commenting obvious things

age += 20 # making "age" 20 years less
>>> # Fix the contradiction

student = "Mark Smith" # we give this variable the value "Mark Smith" because we want to be able to work with it later
>>> # Keep comments concise
```

### 2. Find an unneccessary commnet
Imagine that your skillful friend has created a code for beginner programmers who need to learn more about Python's syntax.<br>
The program raises a given integer to the given power.

Your friend also commented some lines.<br>
Have a look at the code below.<br>
Which of the comments is unnecessary?<br>
Copy it without `#` in the text field below.
```python
integer = 2
power = 8
result = integer ** power  # ** is used for raising to the nth power
print(result)  # print the result 
```

```
print the result
```

### 3. Information sources
Now it's time to use your googling skills and find the information in one of the most important Python documents: **PEP 8**.

Please, find the PEP 8 full text and copy only the first sentence from the section **Comments** of that document.

> The answer should start with "Comments that".<br>
Just [look it up](https://www.python.org/dev/peps/pep-0008/#comments) for yourself!

```
Comments that contradict the code are worse than no comments.
```

### 4. Best Practices
Which methods of improving the readability of code are considered good practices?

> [F] Using not more than 10 comments for a script<br>
> [T] Writing self-explanatory simple code<br>
> [F] Commenting every line of code<br>
> [T] Using human-readable names for variables

### 5. Bad comments
Below you can find three code snippets with different comments.<br>
Unfortunately, all of them are bad!<br>
Match each code label with the explanation.

Code snippet **A**:
```python
month = 'June'  # this variable contains the month
print('I was born in', month)
```

Code snippet **B**:
```python
p = 50  # the age of a person
print('His age is', p)
```

Code snippet **C**:
```python
counter += 4 #inсrease the counter
```

> Answer
```
Code snippet A
>>> The variable is obvious, we don't need to comment it.

Code snippet B
>>> The comment is fine but the name of the variable is not clear.

Code snippet C
>>> Syntax is not in accordance with PEP-8
```

### 6. The number of students
We wrote a simple program that deals with the total number of students in the class and does calculations with it.<br>
This number is stored in the variable `n`.<br>
In the code, it is declared as follows:
```python
n = 10  # stores the number of students in the class
```

What would be a better way of declaring this variable?<br>
And do we need the comment in this case?<br>
Choose the best option.

> [T] `number_of_students = 10`<br>
> [F] `students_num = 10` # stores the number of students in the class<br>
> [F] `st = 10`<br>
> [F] `number_of_students = 10` # the number of students in the class