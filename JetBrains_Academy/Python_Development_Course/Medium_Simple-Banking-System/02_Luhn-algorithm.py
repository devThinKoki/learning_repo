# Description
    # In this stage, we will find out what the purpose of the checksum is and what the Luhn algorithm is used for.
    
    # The main purpose of the check digit is to verify that the card number is valid. 
    # Say you're buying something online, and you type in your credit card number incorrectly by accidentally swapping two digits, which is one of the most common errors. 
    # When the website looks at the number you've entered and applies the Luhn algorithm to the first 15 digits, the result won't match the 16th digit on the number you entered. 
    # The computer knows the number is invalid, and it knows the number will be rejected if it tries to submit the purchase for approval, so you're asked to re-enter the number. 
    # Another purpose of the check digit is to catch clumsy attempts to create fake credit card numbers. 
    # Those who are familiar with the Luhn algorithm, however, could get past this particular security measure.

    # Luhn Algorithm in action
    # The Luhn algorithm is used to validate a credit card number or other identifying numbers, such as Social Security. 
    # The Luhn algorithm, also called the Luhn formula or modulus 10, checks the sum of the digits in the card number and checks whether the sum matches the expected result or if there is an error in the number sequence. 
    # After working through the algorithm, if the total modulus 10 equals zero, then the number is valid according to the Luhn method.

    # While the algorithm can be used to verify other identification numbers, it is usually associated with credit card verification. 
    # The algorithm works for all major credit cards.

    # Here is how it works for a credit card with the number 4000008449433403:
    # https://ucarecdn.com/b2ca8ed0-d7ec-4d72-9043-f60ba6a6cd8b/

    # If the received number is divisible by 10 with the remainder equal to zero, then this number is valid; 
    # otherwise, the card number is not valid. 
    # When registering in your banking system, you should generate cards with numbers that are checked by the Luhn algorithm. 
    # You know how to check the card for validity. 
    # But how do you generate a card number so that it passes the validation test? 
    # It's very simple!

    # First, we need to generate an Account Identifier, which is unique to each card.
    # Then we need to assign the Account Identifier to our BIN (Bank Identification Number). 
    # As a result, we get a 15-digit number 400000844943340, so we only have to generate the last digit, which is a checksum.

    # To find the checksum, it is necessary to find the control number for 400000844943340 by the Luhn algorithm. 
    # It equals 57 (from the example above).
    # The final check digit of the generated map is 57+X, where X is the checksum. 
    # In order for the final card number to pass the validity check, the check number must be a multiple of 10, so 57+X must be a multiple of 10. 
    # The only number that satisfies this condition is 3.

    # Therefore, the checksum is 3. 
    # So the total number of the generated card is 4000008449433403. 
    # The received card is checked by the Luhn algorithm.

    # You need to change the credit card generation algorithm so that card numbers pass the Luhn algorithm.

# Objectives
    # You should allow customers to create a new account in our banking system.

    # Once the program starts you should print the menu:
        # 1. Create an account
        # 2. Log into the account
        # 0. Exit

    # If the customer chooses ‘Create an account’, you should generate a new card number that satisfies all the conditions described above. 
    # Then you should generate a PIN code that belongs to the generated card number.
    # The PIN is a sequence of 4 digits; it should be generated in the range from 0000 to 9999.

    # If the customer chooses ‘Log into account’, you should ask to enter the card information.

    # After the information has been entered correctly, you should allow the user to check the account balance; after creating the account, the balance should be 0. 
    # It should also be possible to log out of the account and exit the program.


# First 6 digits are fixed in our practice which is 400000
# from 7th digits to second to last digits will be generated randomly in the range 000000000 to 999999999
# the final digits will be generated in order to pass Luhn Algorithm check
    # first create 9 digits which exist in the middle of the digits
    # multuply all the odd digits by 2
        # use for loop to check all the digits:
        # sum = 0
        # for idx in range(len(digits9)):
            # if (idx+1) % 2 != 0:
                # digits[idx] *= 2
            # if digits[idx] > 9:
                # digits[idx] -= 9
            # sum += digits[idx]
        # last_digit = 10 - int(sum % 10)
        # card_num = ''.join(['400000'] + [str(i) for i in digits] + [str(last_digit)])

import random
# ################# function & class part ##############
def luhn_Algorithm():
    sum = 0
    digits = list(format(random.randint(400000000000000,400000999999999), '015d'))
    digits_for_check = []
    for idx in range(len(digits)):
        digits_for_check.append(int(digits[idx]))
        if (idx+1) % 2 != 0:
            digits_for_check[idx] *= 2
        if digits_for_check[idx] > 9:
            digits_for_check[idx] -= 9
        sum += digits_for_check[idx]
    last_digit = str(10 - int(sum % 10))
    if last_digit == '10':
        last_digit = '0'
    card_num = ''.join([i for i in digits] + [last_digit])
    return card_num

# # class code for create Card Object
class Card:
    def __init__(self, num = None, PIN = None, bal = 0): 
        if num:
            self.num = num
        else:
            self.num = luhn_Algorithm()
            # self.num = str(random.randrange(4000000000000000,4000010000000000))
        if PIN:
            self.PIN = PIN
        else:
            self.PIN = format(random.randint(0000,9999), '04d')
            # self.PIN = ''.join([str(random.randint(0,10)) for _ in range(4)])
        self.bal = bal

# function is_unique: return whether this created card(new_card) is already exist or not'
# exist means that new_card's 'num' and 'PIN' value are same as one of the existing cards's attribute's value(card and PIN)
def is_unique(new_card, all_cards):
    for card in all_cards:
        if new_card.num == card.num:
            return False
    return True

# if it is unique, this fuction will be executed.
# this function will print some lines and append new_card(object) to all_card(array which contains created card objects)
def create_card(new_card, all_cards):
    print(f"Your card has been created\nYour card number:\n{new_card.num}")
    print(f"Your card PIN:\n{new_card.PIN}")
    all_cards.append(new_card)
    print()

# ask user for card-num and card-PIN and return them
def ask_info():
    num = input("Enter your card number:\n")
    PIN = input("Enter your PIN:\n")
    print()
    return num, PIN

# for given num and PIN, return if there is Card object which has same num and PIN attribute value,
# if not return None
def check_validation(num, PIN, all_cards):
    for card in all_cards:
        if card.num == num and card.PIN == PIN:
            return card
    return None

# show and select main menu and return user input
def show_and_select_main_menu():
    print('1. Create an account\n2. Log into account\n0. Exit')
    menu = input()
    print()
    return menu

# show and select_sub menu and return user input
def show_and_select_sub_menu():
    print('1. Balance\n2. Log out\n0. Exit')
    sub_menu = input()
    print()
    return sub_menu

######################  main part  ###################
# 프로그램이 종료될 때까지 생성된 모든 Card객체를 담는 배열
all_cards = []
# 메인메뉴화면을 출력하고 사용자로 하여금 메뉴선택 입력을 받아 반환하는 함수 호출,
menu = show_and_select_main_menu()
while menu != '0':
    # case1: 메인메뉴에서 1번(계정 생성)을 선택한 경우:
    if menu == '1':
        # 새로운 Card 객체를 생성
        new_card = Card()
        
        # 기존에 있던 카드와 정보가 일치 하지 않으면(고유한 카드이면)
        if is_unique(new_card, all_cards):
            # 카드 객체 생성 후, 카드 객체 배열에 추가
            create_card(new_card, all_cards)
        menu = show_and_select_main_menu()
    
    elif menu == '2':
        num, PIN = ask_info()
        # 입력된 Card 객체의 num과 PIN이 all_cards 배열에 있는 객체가 갖고 있는 값과 일치한다면,
        # card 변수에 해당 정보를 담고 있는 Card 객체가 반환
        card = check_validation(num, PIN, all_cards)
        # card에 Card객체가 정상적으로 담긴 상태라면(정보가 맞다면),
        # 서브 메뉴 선택화면으로 이동
        if card:
            print('You have successfully logged in!')
            print()
            sub_menu = show_and_select_sub_menu()
            while True:
                # Balance(1) 선택시: Card객체의 Balance 속성을 출력 한 뒤, 서브메뉴 while 반복
                if sub_menu == '1':
                    print(f'Balance: {card.bal}')
                    print()
                    sub_menu = show_and_select_sub_menu()
                
                # Log out 선택시: 서브 메뉴 while문 탈출하며, 메인 메뉴 선택화면으로 변경
                elif sub_menu == '2':
                    print('You have successfully logged out!')
                    print()
                    menu = show_and_select_main_menu()
                    break
                # 서브 메뉴에서 '0'을 선택한 경우, 프로그램종료
                elif sub_menu == '0':
                    print('Bye!')
                    exit()
                # 0, 1, 2외의 다른 값을 입력시 다시 서브 메뉴를 표시함
                else:
                    sub_menu = show_and_select_sub_menu()
        # card에 Card객체가 담기지 않았다면(정보불일치),
        # 메인 메뉴 선택 화면으로 이동
        else:
            print('Wrong card number or PIN!')
            print()
            menu = show_and_select_main_menu()
    # if user give value as input() not among '0', '1' nor '2', display menu again
    else:
        menu = show_and_select_main_menu() 

# if user choose '0: Exit' program will close()
print('Bye!')
exit()