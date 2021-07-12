import random

def change_hint(Answer, user_char, hint):
    char_idx = -1
    for _ in range(Answer.count(user_char)):
        char_idx = Answer.find(user_char, char_idx + 1)
        hint[char_idx] = user_char
    return hint

def play_hangman(Answer):
    print('H A N G M A N')
    
    hint = ['-' for i in range(len(Answer))]
    checked, life, correct = set(), 8, False
    while life > 0:
        print()
        print(''.join(hint))
        if ''.join(hint) == Answer:
            correct = True
            break
        user_char = input("Input a letter: ")
        if user_char in Answer:
            if user_char not in checked:
                hint = change_hint(Answer, user_char, hint)
                checked.add(user_char)
            else:
                print("No improvements")
                life -= 1
        else:
            print("That letter doesn't appear in the word")
            checked.add(user_char)
            life -= 1
    if correct:
        print('You guessed the word!')
        print('You survived!')
    else:
        print('You lost!')

answer_list = ['python', 'java', 'kotlin', 'javascript']
play_hangman(random.choice(answer_list))    