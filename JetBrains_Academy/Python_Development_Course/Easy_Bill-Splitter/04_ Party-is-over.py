# Description
    # It's the right time to update your dictionary with new split values to make our "Who is lucky?" feature better. First, we need to recalculate the split value for everyone. Make sure that our lucky one pays 0.

    # Recalculate the split value for n-1 people where n is the total length of the dictionary and update the values in the dictionary with the new split value for everyone.

    # If a user decides not to use the "Who is lucky" feature, print the original dictionary.

# Objectives
    # In this stage your program should perform the following steps together with the steps from the previous stages:
        # In case of an invalid number of people, "No one is joining for the party" is expected as an output;
        # Otherwise, if the user choice is Yes, re-split the bill according to the feature;
        # Round up the split value to two decimal places;
        # Update the dictionary with new split values and 0 for the lucky person;
        # Print the updated dictionary;
        # If the user entered anything else instead of Yes, print the original dictionary.

# Examples
    # The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    # Example 1: The feature is used
        # Enter the number of friends joining (including you):
        # > 5

        # Enter the name of every friend (including you), each on a new line:
        # > Marc
        # > Jem
        # > Monica
        # > Anna
        # > Jason

        # Enter the total bill value:
        # > 100

        # Do you want to use the "Who is lucky?" feature? Write Yes/No:
        # > Yes

        # Jem is the lucky one!

        # {'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}
    
    #  Example 2: The feature is skipped
        # Enter the number of friends joining (including you):
        # > 5

        # Enter the name of every friend (including you), each on a new line:
        # > Marc
        # > Jem
        # > Monica
        # > Anna
        # > Jason

        # Enter the total bill value:
        # > 100

        # Do you want to use the "Who is lucky?" feature? Write Yes/No:
        # > No

        # No one is going to be lucky

        # {'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
    
    # Example 3: Invalid input
        # Enter the number of friends joining (including you):
        # > 0

        # No one is joining for the party


import random
people = dict()
people_in_list = list()
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
        people_in_list.append(name)
    print()

    print('Enter the total bill value: ')
    total_value = int(input())
    n = len(people)
    for key, value in people.items():
        people[key] = round(total_value / n, 2)
    print()

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ")
    answer = input()
    print()

    if answer == 'Yes':
        randomIdx = random.randint(0, len(people_in_list)-1)
        
        Name = people_in_list[randomIdx]
        print(f"{Name} is the lucky one!")
        n -= 1
        for k, v in people.items():
            people[k] = round(total_value / n, 2)
        people[Name] = 0
    else:
        print("No one is going to be lucky")
    
    print()
    print(people)