# Sep and end arguments of print
You already know that, to print out objects, you can use the `print()` function.<br>
For example, the following lines of code will show us the value of a variable:
```python
number = 5
print(number)  # 5
```

But did you know that `print()` can take multiple keyword arguments?

## 1. The separator
For example, with the `sep` argument you can specify the separator between objects to be printed (the separator itself must be a string).
```python
print('Chip', 'Dale', sep='&')  # Chip&Dale
print('Chip', 'Dale', sep=0)    # TypeError: sep must be None or a string, not int
```

The default value of this argument is space, that is, writing `print('Gadget', 'Hackwrench', sep=' ')` gives the same output as writing `print('Gadget', 'Hackwrench')`:
```python
print('Gadget', 'Hackwrench', sep=' ')
# Gadget Hackwrench

print('Gadget', 'Hackwrench')
# Gadget Hackwrench
```

You can also use an empty string as `sep` when you want to print several objects together:
```python
print(13, 'th', sep='')  # 13th
```

It will work even if you combine different values, such as integers and strings, in the example above.

## 2. The end
The argument `end` determines how the string we want to print should end.<br>
The default value is `'\n'`, which means that it ends with a newline.<br>
So if you give no arguments to the function and simply write `print()`, it will shift you to a new line:
```python
print('Monterey')
print()
print('Jack')
```

The output will be as follows:
```
Monterey

Jack
```

However, just as with the `'sep'` argument, we can set this argument to end with any other string.
```python
print('Tick-Tock', end=' the ')
print('Crocodil', end='e')
# Tick-Tock the Crocodile
```

## 3. Unpacking objects
The first arguments of the `print()` function are objects we want to print.<br>
For example, if it's a list `characters = ['Humphrey the Bear', 'Spike the Bee', 'Fat Cat']`, writing `print(characters)` will yield the output `['Humphrey the Bear', 'Spike the Bee', 'Fat Cat']`.<br>
But what if we want to print objects from a list, not the list as a whole?<br>
One way would be to use a loop:
```python
for element in characters:
    print(element)
```

However, in Python, there's a more convenient and neat way to do so. Writing an asterisk * before a list means that its elements will be unpacked and passed to the function one after another:
```python
print(*characters)
```

An important detail to understand, however, is that, in the first case, the elements will be printed one in one line, whereas in the second case, they will be separated by spaces.<br>
This is so because the first snippet of code is equivalent to writing these lines with the default `end="\n"`:
```python
print('Humphrey the Bear')
print('Spike the Bee')
print('Fat Cat')
```

while the second one could be replaced by the line `print('Humphrey the Bear', 'Spike the Bee', 'Fat Cat')` with the default `sep=' '`:
```python
print(*characters)
# Humphrey the Bear Spike the Bee Fat Cat
```

## 4. Summary
We rediscovered the built-in `print()` function and examined some of its arguments, `sep` and `end`.

> Note that the mentioned arguments are so-called keyword arguments.<br>
> You should explicitly specify them when calling the function because all other (positional) arguments are considered as objects to be printed.<br>

As you can see, arguments of the `print()` function provide useful ways of managing output.<br>
Keep that in mind when working with strings!

## 5. Practices
### 1. Letter-spacing
Let's do some text formatting.<br>
Read an input word and print it with an indicated number of spaces between the letters.<br>
There are two different inputs: a word in the first line and a number of spaces in the second line.

> Note that unpacking works for strings as well.<br>
And to get the exact number of spaces, multiply the string by that number: `' ' * number_of_spaces`

### **Sample Input 1**:
```
earnest
1
```
### **Sample Output 1**:
```
e a r n e s t
```

### **Sample Input 2**:
```
Ernest
2
```
### **Sample Output 2**:
```
E  r  n  e  s  t
```

```python
str_ = input()
number_of_spaces = int(input())
print(str_, sep=' '*number_of_spaces)
```

### 2. Writing a name
You are given a list containing letters of a `name`.<br>
Print them out as a string with these chars separated by hyphens and with an exclamation point in the end.<br>
Do so using arguments of the `print()` function!

So, if the letters in the list name are `['K', 'A', 'T', 'E']`, your program should print the string `'K-A-T-E!'`

```python
name = ['M', 'A', 'R', 'C', 'O']
# modify the next line
# print(...)
print(*name, sep="-", end="!")
```
### 3. Greetings
Imagine you have string variables:
```python
adj = "Good"
part_of_day = "morning"
comma = ","
title = "Ms."
surname = "Johnson"
```

And you need to print out a greeting `"Good morning, Ms. Johnson!"` (without the quotes) calling the `print()` function only once and specifying its keyword arguments, without adding any other strings.<br>
How would you do that?

> Concatenate strings if necessary.
```python
adj = "Good"
part_of_day = "morning"
comma = ","
title = "Ms."
surname = "Johnson"

# your print() function
# print(...)
print(adj, part_of_day + comma, title, surname, sep=" ", end="!")
```

### 4. Combining seps & ends
Choose all pieces of code that will yield the following output: `a_b_c_`.
#### Answer
- [F] print('a', '_', 'b', '_', 'c', end='_')
- [T] print('a', end='')<br>
    print('_', '_', sep='b', end='c_')
- [F] print('a', sep='_')<br>
    print('b', sep='_')<br>
    print('c', sep='_')
- [T] print('a', 'c', sep='_b_', end='_')
- [T] print('a', 'b', 'c', sep='_', end='_')

### 5. Stick together
You are given a list of numbers.<br>
Print them out together.

> Set an empty line to one of the `print()` arguments, either to `sep` or `end`.<br>
There is a solution with each of these options. 

### **Sample Input 1**:
```
1 2 3 4 5 6 7 8 9
```
### **Sample Output 1**:
```
123456789
```

```python
numbers = [int(x) for x in input().split()]
# print all numbers without spaces
print(*numbers, sep='')
print(*numbers, end='')
```

### 6. Several lines, one print
Write a snippet that will print the following lines using only one `print()` statement.

The lines:
```
Night, square, apothecary, lantern,
Its meaningless and pallid light.
Return a half a lifetime after –
All will remain. A scapeless rite.
```

```python
line1 = "Night, square, apothecary, lantern,"
line2 = "Its meaningless and pallid light."
line3 = "Return a half a lifetime after – "
line4 = "All will remain. A scapeless rite."

# your one print() statement here
print(line1, line2, line3, line4, sep='\n')
```