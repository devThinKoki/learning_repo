# Objects in Python
Knowing how different types of objects work in Python will help you understand some of the following topics more deeply, as well as the structure of the language in general.

## 1. Reference to an object
In Python, all values are stored in objects.
You can think that an object is like a box that contains information about some value and also stores some additional data such as its identity.
When you assign a value to a variable, e.g. `string = "hello"`, Python creates a new object, places this value (the string `"hello"` in our case) inside the new object and then creates a **reference** from the variable name `string` to the object.

![](https://ucarecdn.com/657a40a1-4ae3-44a2-b484-caaa762c635d/)

Then, if we assign one variable to another, e.g. `new_string = string,` Python will create a reference from the new variable `new_string` to the **same_object.**

![](https://ucarecdn.com/facfeced-a7b5-47b2-9e94-cc241fe3aac0/)

You can use the `id` function to see that both variables refer to the same object:
```python
print(id(string))        # 4336233024
print(id(new_string))    # 4336233024
```
As a result, you can access the object using any of the two variable names.
You can also assign a new value to one of these variables and this will not affect the other one.

```python
string = "hello"
new_string = string
string = "world"

print(string, id(string))            # world 4336233136
print(new_string, id(new_string))    # hello 4336233024
```
Note that the identity has changed along with the value.

![](https://ucarecdn.com/7f9aff54-a941-4cff-89cc-a76ddb3a1a4e/)

However, the situation is a bit more complex when we deal with mutable objects, e.g. some of the containers.

## 2. Mutable objects & references
Let's take a list as an example.
The thing is, a list doesn't store its values inside itself.
Instead, it stores **references** to objects that store values.
For example, when you write `lst = [2, 3, 9]`, Python creates the following structure:

![](https://ucarecdn.com/422bb28f-ef2f-4a8a-9326-651fd26a7ccd/)

Now, if we assign our list to a new variable and then try to alter the first object, this will also affect the new list:
```python
lst = [2, 3, 9]
new_lst = lst

print(lst, id(lst))            # [2, 3, 9] 4334518600
print(new_lst, id(new_lst))    # [2, 3, 9] 4334518600

# we change an element of the first list
lst[2] = 0
print(lst, id(lst))            # [2, 3, 0] 4334518600

# but the new list is also modified
print(new_lst, id(new_lst))    # [2, 3, 0] 4334518600
```

This is so because both lists refer to the same object: when it is modified, all variables continue to refer to this very object.
In the next topic, you will learn how to alter a list without changing its copies.

## 3. Summary
- Variables in Python do not store values themselves, they store **references** to objects that store values.
- When we assign one variable to another, they refer to the **same object**.
- After modifying mutable objects, other variables referring to it will also **change**.

## 4. Practices
### 1. Black box
There's a function `blackbox(lst)` that takes a list, does some magic, and returns a list.
You don't know if it modifies the given list or creates a completely different one.
Find this out and print `"modifies"` if the function changes the given list or `"new"` if the returned list is not connected to the initial one.

Remember to define your list.
Content is not important.

> You should create your own list, then call the `blackbox()` function on it to get the second list, and finally compare the two lists.

```python
# use the function blackbox(lst) that is already defined
my_list = [1, 3, 5]
returned_list = blackbox(my_list)
if id(my_list) == id(returned_list):
    print("modifies")
else:
    print("new")
```

### 2. Value of b
Lists, unlike strings, are mutable.
We can use that to modify their data with indexes.

Here's a simple piece of code.
What will be the value of `b` after each line of code?
```python
a = [1, 2, 3]
b = a
# what is the value of b?

a[1] = 10
# and here?

b[0] = 20
# what about now?

a = [5, 6]
# it is the last time, we promise. The value of b?
```

Please, enter the values in a single line. Separate the list elements with space and the lists — with a semicolon.
For example:
- 1 1 1; 2 2 2; 3 3 3; 4 4 4

> Since `b = a`, they refer to the same object.

- Answer
```
1 2 3; 1 10 3; 20 10 3; 20 10 3
```

### 3. Check references
Imagine, you have two variables and you don't know what they contain but need to check if they refer to the same object or not.
How would you do that?

Write a function `check(obj1, obj2)` that will take two objects and print `True` if they refer to the same object and `False` otherwise.

```python
def check(object_1, object_2):
    if id(object_1) == id(object_2):
        print('True')
    else:
        print('False')
```
### 4. The same list?
Let's say we have a list with grades of a student:
```python
grades = [10, 7, 8, 7, 9, 6]
id1 = id(grades)              # 41602624
```
Then, the student retook the last exam, and the grade became better:
```python
grades[-1] = 9
print(grades)       # [10, 7, 8, 7, 9, 9]
id2 = id(grades)
```
Will `id2` be the same as `id1`?
Please write `yes` or `no` in the text field below.
```
yes
```

### 5. Number of objects
Look at the following piece of code:
```python
today = "monday"
tomorrow = "tuesday"
today = tomorrow
tomorrow = today
```
How many different objects are created here in total?
```
2
```

### 6. Ids of even numbers
Imagine you have a list in which you can find different integers.
You created a code that prints an id of an even integer.
Unfortunately, the lines are jumbled. 
Order them!
- Original
```
print(id(integer))
if integer % 2 == 0:
for integer in integers:
integers = [2, 23, 4, 5, 6, 97, 45, 31, 50]
```

- Answer
```python
integers = [2, 23, 4, 5, 6, 97, 45, 31, 50]
for integer in integers:
    if integer % 2 == 0:
        print(id(integer))
```

