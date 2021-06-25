# Description
#   You have planned a dinner with your friends today. It's the right time to add them to your program. You need to be sure how many friends are joining you for dinner including you.
#   The idea is to take names from user input. Store them in a dictionary.
#   For example, if five friends are joining including you, you need to add five people to the dictionary so that you can access/update the corresponding bill value later.

# Objectives
#   In this stage your program should perform the following steps:
#       Take user input — how many people want to join, including the user;
#       In case of an invalid number of people (zero or negative), "No one is joining for the party" is expected as an output;
#       Otherwise, take the friends' names as input, iteratively;
#       Store them in a dictionary initialized with zeros;
#       Print out the dictionary.
#   To communicate with the user, please use the prompts specified in the examples. Note that here and in the following stages we expect you to take every input in a new line.

# Examples
#   The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

#   Example 1: Valid input
#       Enter the number of friends joining (including you):
#       > 5

#       Enter the name of every friend (including you), each on a new line:
#       > Marc
#       > Jem
#       > Monica
#       > Anna
#       > Jason

#       {'Marc': 0, 'Jem': 0, 'Monica': 0, 'Anna': 0, 'Jason': 0}

#   Example 2: Invalid input

#       Enter the number of friends joining (including you):
#       > 0

#       No one is joining for the party

people = dict()
print("Enter the number of friends joining (including you):")
how_many = int(input())
print()

if how_many <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(how_many):
        name = input()
        people[name] = 0
    print()
    print(people)