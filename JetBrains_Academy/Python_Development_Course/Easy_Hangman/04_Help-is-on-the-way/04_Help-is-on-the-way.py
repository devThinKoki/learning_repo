# ##### Version 1 #####
# import random
# words = ['python', 'java', 'kotlin', 'javascript']
# chosen_word = random.choice(words)
# # print(chosen_word)
# first_3_letters = chosen_word[:3]

# guessing = input(f'''H A N G M A N
# Guess the word {first_3_letters}{'-' * (len(chosen_word) - 3)}: ''')
# if guessing == chosen_word:
#     print('You survived!')
# else:
#     print('You lost!')

##### Version2 #####
import random
def play_hangman(Answer):
    user = input(f'''H A N G M A N
Guess the word {hint_word(Answer)}: ''')
    if user == Answer:
        print('You survived!')
    else:
        print('You lost!')

def hint_word(word):
    length = len(word) - 3
    word = word[:3] + '-' * length
    return word

answer_list = ['python', 'java', 'kotlin', 'javascript']
play_hangman(random.choice(answer_list))


# try:
#     name, surname = input().split()
#     print(f'Welcome to our party, {name} {surname}')
# except ValueError as e:
#     print('You need to enter exactly 2 words. Try again!')
# print('You will be more than welcome!')


# def what_to_do(instructions):
#     simon = 'Simon says'
#     if instructions.startswith(simon):
#         print(f'I {instructions[len(simon) + 1:]}')
#     elif instructions.endswith(simon):
#         print(f"I {instructions[:len(instructions) - len(simon)]}")
#     else:
#         print("I won't do it!")
# what_to_do("make a wish Simon says")
# what_to_do("Go away")
# what_to_do('Simon says')