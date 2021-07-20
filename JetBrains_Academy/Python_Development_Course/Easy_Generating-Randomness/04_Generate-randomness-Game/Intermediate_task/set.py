print('-'*20, 'EX01', '-'*20)
# Eugene and Rose decided to travel abroad. 
# For convenience, they will go to a country where one of them has already been, but not where they both have.

# Output a set of potential countries for them.

# Sample Input 1:
    # Greece Netherlands Colombia UK
    # Italy UK Russia Greece Canada
# Sample Output 1:
    # {'Colombia', 'Russia', 'Italy', 'Netherlands', 'Canada'}
eugene, rose = set(input().split()), set(input().split())
print(eugene.symmetric_difference(rose))


print('-'*20, 'EX02', '-'*20)
# There's a hidden variable with top secret data.
# You can't see it, and all you know about it is that it's called `pentagon_passwords` and that it is a container with sets.
# Try to get the intersection of these sets and output the number of elements in it.

# >>> print(len(set.intersection(*pentagon_passwords)))


print('-'*20, 'EX03', '-'*20)
# Write down the command that should be put instead of ... to get a set of symbols that the set a and the string b both contain.
# ````
a = set("my code is brOKen")
b = "i'm not OK with that"
# c = ...
# ````
# Do NOT convert b to a set in your solution, it should remain a string.

# >>> a.intersection(b)


print('-'*20, 'EX04', '-'*20)
# What is the difference between using an operator and a set operation method?
# [F] 1. Only operators can be used to update an existing set
# [T] 2. Only methods can accept a bunch of sets at once, in a certain way
# [T] 3. The difference is in the syntax.
# [F] Only operators can work with non-set arguments


print('-'*20, 'EX05', '-'*20)
# Imagine you have two lists of names: 
    # people from the first list play the violin, while people from the second one happen to speak German.

# Print a set with names of those who can do both.
# Sample Input 1:
    # Vanessa-Mae, David Garrett
    # Rosamond Mayhan, Malik Kopf, David Garrett, Cortez Mestas, Barbara Miller, Elease Knudson
# Sample Output 1:
    # {'David Garrett'}
violinists = set(input().split(', '))
german_speakers = set(input().split(', '))
print(violinists.intersection(german_speakers))


print('-'*20, 'EX06', '-'*20)
# Match the names of the methods with the corresponding operators.
    # intersection  &
    # union         |
    # update        |=
    # difference    -


print('-'*20, 'EX07', '-'*20)
# Using the three given sets, write a code that creates a set containing the elements that all of the original sets have in common.
# Output this resulting set.

# NB! You don't need to read the input; the variables containing the input data are already created for you.

# Sample Input 1:
    # Jupiter Saturn Mars
    # Earth Mars Venus
    # Mars Pluto Uranus
# Sample Output 1:
    # {'Mars'}
set_1 = set(input().split())
set_2 = set(input().split())
set_3 = set(input().split())
print(set.intersection(*[set_1, set_2, set_3]))


print('-'*20, 'EX08', '-'*20)
# You are given several sets with names of students in different classes. 
# Output the set containing names of all the students.

# NB! You don't need to read the input; the variables containing the input data are already created for you.

# Sample Input 1:
    # Potter Weasley
    # Lovegood Corner
    # Malfoy Goyle
    # Bones Macmillan
# Sample Output 1:
    # {'Potter', 'Weasley', 'Lovegood', 'Corner', 'Malfoy', 'Goyle', 'Bones', 'Macmillan'}
gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())
print(gryffindor | ravenclaw | slytherin | hufflepuff)


print('-'*20, 'EX09', '-'*20)
# Some states of the USA share their names with rivers.
# We have defined two variables with respective place names.

# Print out a new set with river names that don't overlap with given states.

# Sample Input 1:
    # Alabama Missouri Mississippi
    # Georgia Alaska Missouri
# Sample Output 1:
    # {'Alabama', 'Mississippi'}
rivers = set(input().split())
states = set(input().split())
print(rivers - states)


print('-'*20, 'EX10', '-'*20)
# What is the name of the operation that returns a new set filled with objects that only one of the original sets had?
# [F] intersection_update
# [T] difference
# [F] difference_update
# [F] union