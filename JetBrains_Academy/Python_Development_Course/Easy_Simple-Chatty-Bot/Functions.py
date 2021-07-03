def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")

    name = input()
    print(f"What a great name you have, {name}!")

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    n1, n2, n3 = int(input()), int(input()), int(input())
    age = (n1 * 70 + n2 * 21 + n3 *15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

def count(): 
    print("Now I will prove to you that I can count to any number you want.")

    num = int(input())
    curr = 0
    while curr <= num:
        print(f"{curr}, !")
        curr += 1

def test():
    print("Let's test your programming knowledge.")
    # write code here.
    Question = """What is the date of today?
1. 2021-07-01
2. 2020-07-03
3. 2021-07-02
4. 2021-07-03
5. 2020-07-04"""
    print(Question)
    while True:
        answer = int(input())
        if answer == 4:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again")

def end():
    print("Congratulations, have a nice day!")