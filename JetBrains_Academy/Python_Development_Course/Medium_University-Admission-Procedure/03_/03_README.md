## ***Need Skills***
- Escape sequences
- Arguments
- Operations with list
- While loop
- Loop control statements
- ***Lambda functions***
- List comprehension
- ***Nested lists***
- ***Split and join***
- ***Iterators***
- ***Ordering and total order***
- ***Sorting a list***

# Goal
- Now you'll have to deal with a whole list of applicants instead of just one!<br>
Find the lucky ones by comparing their GPA score.

# Description
- Things are heating up!<br>
Our university has become trendy, so the applicants are rushing in.<br>
Your program has to be adapted to this — unfortunately, we cannot enroll everybody.<br>
The program will need to rank the potential students and determine who's going to get admitted.<br>
At this stage, you'll need to work with the Grade Point Average (GPA).<br>
It is the mean grade of all high school courses.<br>
We don't need the threshold, for now, a certain number of applicants with the best GPA will be accepted instead.

# Theory
- To proceed further we need to understand the basics of sorting.<br>
To use more than one attribute for list sorting, use the following syntax:<br>
```
not_sorted_list = [['c', 11], ['a', 11], ['c', 10]]
sorted_list = sorted(not_sorted_list, key = lambda x: (x[0], x[1]))
print(sorted_list)
# [['a', 11], ['c', 10], ['c', 11]]
```
- In this example, the first value (`x[0]`) of each element of the `not_sorted_list` is used for sorting in the first place.<br>
If these values are equal, the second value (`x[1]`) is used to determine which element is greater.

- A problem may occur if you want to sort the list in ascending order by the first value and in the descending order by the second value.<br>
For example, you have two values to sort the list by: 
    - score and time.
```
# the first element in each nested list is score
# the second element is time
not_sorted_list = [[531, 11.76], [401, 5.11], [531, 10.05]]
```
- You want to sort your list in such a way that the elements with the highest score and the smallest time value would go before the elements with a lower score and greater time value.<br>
To do this, you can simply inverse one of the values by adding a minus in front of it:
```
# both lines will lead to the same result
sorted_list = sorted(not_sorted_list, key = lambda x: (-x[0], x[1]))
sorted_list = sorted(not_sorted_list, reverse=True, key = lambda x: (x[0], -x[1]))
print(sorted_list)
# [[531, 10.05], [531, 11.76], [401, 5.11]]
```

# Objective
- At this stage, your program should:
    1. Read the first input, an **N** integer representing the total number of applicants.
    1. Read the second input, an **M** integer representing the number of applicants that should be accepted to the university.
    1. Read **N** lines from the input.<br>
    Each line contains the first name, the last name, and the applicant's GPA.<br>
    These values are separated by one whitespace character.<br>
    A GPA is a floating-point number with two decimals.
    1. Output the `Successful applicants:` message.
    1. Output **M** lines for applicants with the top-ranking GPAs.<br>
    Each line should contain the first and the last name of the applicant separated by a whitespace character.<br>
    Successful applicants' names should be printed in descending order depending on the GPA — first, the applicant with the best GPA, then the second-best, and so on.
    1. If two applicants have the same GPA, rank them in alphabetical order using their full names (we know it's not really fair to choose students by their names, but what choice do we have?)
    
# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

- Example 1
```
> 5
> 3
> Cole Collins 3.68
> Dolores Baldwin 3.40
> Brett Boyer 2.45
> Nora Alston 3.71
> Jessy Moore 3.14
Successful applicants:
Nora Alston
Cole Collins
Dolores Baldwin
```
- Example 2 : applicants with equal GPA, note that the full name is used to sort these applicants
```
> 3
> 2
> Albert Collins 3.02
> Albert Nelson 3.02
> Cole Allen 3.02
Successful applicants:
Albert Collins
Albert Nelson
```