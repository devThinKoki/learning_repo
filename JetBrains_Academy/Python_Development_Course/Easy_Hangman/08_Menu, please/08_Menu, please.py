import random
import string

def change_hint(Answer, user_char, hint):
    char_idx = -1
    for _ in range(Answer.count(user_char)):
        char_idx = Answer.find(user_char, char_idx + 1)
        hint[char_idx] = user_char
    return hint

def play_hangman(Answer):
    print('H A N G M A N')
    while True:
        menu = input('Type "play" to play the game, "exit" to quit: ')
        if menu == 'play':
            break
        elif menu == 'exit':
            exit()

    hint = ['-' for i in range(len(Answer))]
    checked, life, correct = set(), 8, False
    while life > 0:
        print()
        print(''.join(hint))
        if ''.join(hint) == Answer:
            correct = True
            break
        user_char = input("Input a letter: ")
        if len(user_char) != 1:
            print("You should input a single letter")
        elif user_char not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
        elif user_char in checked:
            print("You've already guessed this letter")
        elif user_char not in Answer:
            print("That letter doesn't appear in the word")
            checked.add(user_char)
            life -= 1
        else:
            hint = change_hint(Answer, user_char, hint)
            checked.add(user_char)

    if correct:
        print('You guessed the word!')
        print('You survived!')
    else:
        print('You lost!')

answer_list = ['python', 'java', 'kotlin', 'javascript']
play_hangman(random.choice(answer_list))    