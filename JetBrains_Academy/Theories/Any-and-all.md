# Any and all
By now, you certainly know that Python has a lot of different **built-in functions** that help developers work more efficiently.<br>
Built-in functions are always available, so you don't need to declare or import them.<br>
Just call such a function whenever you need it.<br>
You have already seen one of those functions, it is `print()`.<br>
Today we will learn two more built-in functions `any()` and `all()` and find out how and when to use them.

Be careful though, these functions work only with **iterable objects**, e.g. strings and lists.<br>
A list is iterable, so we will use it to illustrate the theoretical part and to show how `any()` and `all()` work.

## 1. Function any()
The result of the `any()` function call is the boolean value: it returns `True` if an element or a group of elements in an iterable object are evaluated `True`.<br>
Otherwise, it returns `False`.<br>
Let’s take a look at the example.<br>
Imagine that you and your friends, Jam and Andy, wrote a test and got your results in the form of a list with `True` and `False` values.<br>
The test is passed if at least one answer is correct.<br>
Now you need to check if you and your friends passed that test.
```python
your_results = [True, False, False]
print(any(your_results))  # True
```

As you know, the value `True` corresponds to 1, while `False` can be represented by 0, therefore, you can replace the boolean values with the numerical ones in the list above and get the same result.
```python
your_results = [1, 0, 0]
print(any(your_results))  # True
```

In fact, all numbers other than 0 will be regarded as `True`, even the negative ones.<br>
That part stems from how the [bool()](https://docs.python.org/3/library/functions.html#bool) function works.

Now back to our test example, you passed with one correct answer.<br>
What about your friends, Jam and Andy?<br>
Andy has a different list of results to check.
```python
andy_results = [False, False, False]
print(any(andy_results))  # False
```

Unfortunately, your friend Andy failed.<br>
What about Jam?<br>
Well, this friend of yours didn't write the test at all, so he got an empty list of results.
```python
jam_results = []
print(any(jam_results))  # False
```

The list doesn't contain any elements, and since no `True` value is to be found the `any()` function returns `False`.

So what does the `any()` function do?<br>
First, it takes a list as an argument, then evaluates all the elements of this list to find at least one `True`, if so, it returns `True`, otherwise, the result is `False`.

## 2. Function all()
The `all()` function works pretty much like `any()`.<br>
The difference is that `all()` function checks if all the elements of an iterable object are `True` and returns `True` if they are.<br>
Otherwise, you get `False`.<br>
Do you remember the story from the previous section where we checked the results of the test?<br>
Let's proceed.<br>
Imagine yet another test, this time the final one.<br>
To succeed, you should answer all the questions correctly.<br>
How did it go this time for you and the two friends of yours?
```python
your_results = [True, False, False]
print(all(your_results))  # False
```

As you can see, not all the answers in your case are correct, so you didn't pass the test.<br>
What about Andy's results?
```python
andy_results = [True, True, True]
print(all(andy_results))  # True
```

Luckily, Andy passed.<br>
Jam seems to have a vacation.<br>
His list of results is empty again.
```python
jam_results = []
print(all(jam_results))  # True
```

The list doesn't contain any elements, but the `all()` function will return `True` because it searches for any `False` values.<br>
No `False` values result in `True`.<br>
Be careful with this scenario.

## 3. Non-boolean values
Pay attention to the fact that `any()` and `all()` can take a list containing non-boolean values.<br>
Let's recall how they are evaluated.

Empty sequences, e.g. strings and lists, as well as zero, are equivalent to `False`, the same applies to the constant `None`.<br>
Non-empty sequences are equivalent to `True`.

> Be cautious, the result of calling the `all()` function on an empty sequence differs from converting an empty sequence to a boolean value.<br>
> The result of `all(list())` is `True`, the result of `bool(list())` is `False`.

Here is a list with false values.<br>
`any()` and `all()` will have the same behavior in this example:
```python
rocket_science_scores = [0, -0, 0.0, +0]
any(rocket_science_scores)  # False
all(rocket_science_scores)  # False
```

Now, let's look at the scores of some simpler subject:
```python
math_scores = [0, 1, 2, 3]
any(math_scores)  # True
all(math_scores)  # False
```

As shown, `all()` doesn't return `True` bfor a list where false values are present.<br>
Consider the last case:
```python
biology_scores = [1, 2, 3, 4]
any(biology_scores)  # True
all(biology_scores)  # True
```

The list `biology_scores` has no false values, that's why both functions result in True.

Also, you can turn the elements of your list into the boolean values via comparison.<br>
Suppose, we have a list of scores and want to check whether some are equal to 3 or greater.<br>
It can be done like this:
```python
scores = [1, 2, 3, 4]
boolean_scores = [score >= 3 for score in scores]  # [False, False, True, True]
print(any(boolean_scores))  # True
print(all(boolean_scores))  # False
```

However, lists may contain different elements, e.g. strings or nested lists, in such cases, the behavior of `any()` and `all()` would depend largely on the contents.<br>
Keep that in mind.

## 4. Conditions
Coders often use `any()` and `all()` functions in conditions.<br>
It helps to check the elements of iterable objects quickly and to avoid complex constructions.

Let's choose a candy box for Valentine's Day.<br>
Each box contains several types of sweets.<br>
But you are interested in the even amount of candies of each type because, obviously, you will share them with your valentine.
```python
box = [10, 20, 33]

if any([candy % 2 for candy in box]):
    print("It is not a proper gift.")
else:
    print("Perfect!")
```

Short and sweet, isn't it?<br>
Life is like a box of chocolates!<br>
As long as the values you deal with can be converted to `True` and `False`, it's safe to use both functions in conditions.

## 5. Summary
We learned what `any()` and `all()` functions can do and how they work.<br>
As you can see, these functions are an efficient tool that helps check conditions and may improve the readability of your code.

## 6. Practices
### 1. Objects
Which objects can you use with the functions `any()` and `all()`?

> Objects should be iterable.

#### Answer
- [T] list
- [F] float
- [F] integer
- [F] NaN
- [T] string

### 2. Return value
What will `any()` function return if you apply it to an empty list?

#### Answer
- [F] TypeError
- [F] True
- [T] False
- [F] None

### 3. Lottery
Imagine that you have bought a bunch of lottery tickets and wrote down their numbers into the list. <br>
Now, it's time to figure out whether you have a winning ticket.

You know that all winning tickets are no less than 44.<br>
Fill the empty fields in the code (these ones `...`) to check if you have at least one winning ticket.

You **DON'T** need to print the answer.
```python
# As luck would have it
tickets = [11, 22, 33, 44, 55]
winning_tickets = [i >= 44 for i in tickets]
tickets_bool = any(winning_tickets)
```

### 4. Built-ins
Why are `any()` and `all(`)` called built-in functions?

#### Answer
- [F] You should declare these functions before using.
- [F] Without importing, any() and all() are NOT available.
- [T] You are NOT supposed to declare or import these functions.
- [F] These functions can take another function as an argument.

### 5. Non-boolean
What will `any()` function return if we pass as its argument this string `"the object"`?

#### Answer
- [F] False
- [F] "the object"
- [F] None
- [T] True

### 6. Heads or Tails
We have tossed a coin 6 times and saved the results in a list called `heads_or_tails`<br>.
The values are integers: **1** stands for a head, while **0** denotes a tail.

Add some code to find out whether the list has ***any*** heads.<br>
Do not print the variable `check`, just store the result in it.

```python
# Fingers crossed
check = any(heads_or_tails)  # are there any heads in the list heads_or_tails?
```

### 7. Competition
Today you are taking part in the chess competition.<br>
The winner of the competition will get the `'winner'` status and the largest amount of money if they win all the games.<br>
Much is at stake!

The results are stored in a list.<br>
Fill the blanks in the code below and figure out how much money you won.

You **DON'T** need to print the answer.

```python
check = any([True, True, 1, 1, True])

if check:
    status = 'winner'
else:
    status = 'loser'

if status == 'winner':
    winning_sum = 100
else:
    winning_sum = 10
```

### 8. Prime numbers
In math, we call a natural number prime if it's greater than **1** and can be divided without any remainder only by **1** and itself:
```
2, 3, 5, 7, 11, 13, 17, ...
```

Create a list of all prime numbers up to **1000** in the code below.<br>
Just save this list into a variable `prime_numbers`, you don't have to print anything.

Make use of `any()` or `all()` to check if a number **n** leaves a zero remainder when divided by values from **2** to **n - 1** (inclusively).

```python
prime_numbers = [number for number in range(2, 1001) if all(number % i != 0 for i in range(2, number))]
```