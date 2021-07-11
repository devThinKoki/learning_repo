import random
words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(words)
# print(chosen_word)

guessing = input('''H A N G M A N
Guess the word: ''')
if guessing == chosen_word:
    print('You survived!')
else:
    print('You lost!')