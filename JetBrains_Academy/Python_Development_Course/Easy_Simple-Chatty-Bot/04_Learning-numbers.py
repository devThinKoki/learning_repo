def guess_age(n1, n2, n3):
    return ((n1 * 70) + (n2 * 21) + (n3 * 15)) % 105
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')
your_name = input()

print(f'What a great name you have, {your_name}!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
# reading all remainders
n1, n2, n3 = int(input()), int(input()), int(input())
your_age = guess_age(n1, n2, n3)
print(f"Your age is {your_age}; that's a good time to start programming!")

print(f"Now I will prove to you that I can count to any number you want.")
num = input()
for i in range(int(num) + 1):
    print(f"{i} !")
print("Completed, have a nice day!")