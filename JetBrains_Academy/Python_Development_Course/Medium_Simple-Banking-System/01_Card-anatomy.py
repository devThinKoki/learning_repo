# Description
    # We live busy lives these days.
    # Between work, chores, and other things on our to-do lists, it can be tough to catch your breath and stay calm.
    # Credit cards are one of the things that save us time, energy, and nerves.
    # From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways. 
    # In this project, you will develop a simple banking system with a database.

    # If you’re curious about business, technology, or how things around you work, you'll probably enjoy learning how credit card numbers work. 
    # These numbers ensure easy payments, and they also help prevent payment errors and fraud. 
    # Card numbers are evolving, and they might look different in the near future.

    # Let's take a look at the anatomy of a credit card:
    # ---------------------------------------------------------------    
    # The very first digit is the Major Industry Identifier (MII), 
    # which tells you what sort of institution issued the card.
        # 1 and 2 are issued by airlines
        # 3 is issued by travel and entertainment
        # 4 and 5 are issued by banking and financial institutions
        # 6 is issued by merchandising and banking
        # 7 is issued by petroleum companies
        # 8 is issued by telecommunications companies
        # 9 is issued by national assignment
    # In our banking system, credit cards should begin with 4.
    # ---------------------------------------------------------------
    # The first six digits are the Issuer Identification Number (IIN). 
    # These can be used to look up where the card originated from. 
    # If you have access to a list that provides detail on who owns each IIN, you can see who issued the card just by reading the card number.

    # Here are a few you might recognize:
        # Visa: 4*****
        # American Express (AMEX): 34**** or 37****
        # Mastercard: 51**** to 55****
    # In our banking system, the IIN must be 400000.
    # ---------------------------------------------------------------
    # The seventh digit to the second-to-last digit is the customer account number. 
    # Most companies use just 9 digits for the account numbers, but it’s possible to use up to 12. 
    # This means that using the current algorithm for credit cards, the world can issue about a trillion cards before it has to change the system.

    # We often see 16-digit credit card numbers today, but it’s possible to issue a card with up to 19 digits using the current system. 
    # In the future, we may see longer numbers becoming more common.

    # In our banking system, the customer account number can be any, but it should be unique. 
    # And the whole card number should be 16-digit length.
    # ---------------------------------------------------------------
    # The very last digit of a credit card is the check digit or checksum.
    # It is used to validate the credit card number using the Luhn algorithm, 
    # which we will explain in the next stage of this project. 
    # For now, the checksum can be any digit you like.

# Objectives
    # You should allow customers to create a new account in our banking system.

    # Once the program starts, you should print the menu:
        # 1. Create an account
        # 2. Log into account
        # 0. Exit

    # If the customer chooses ‘Create an account’, 
        # you should generate a new card number which satisfies all the conditions described above. 
        # Then you should generate a PIN code that belongs to the generated card number. 
        # The PIN code is a sequence of any 4 digits. 
        # PIN should be generated in a range from 0000 to 9999.

    # If the customer chooses ‘Log into account’,
        # you should ask them to enter their card information. 
        # Your program should store all generated data until it is terminated so that a user is able to log into any of the created accounts by a card number and its pin.
        # You can use an array to store the information.

    # After all information is entered correctly, 
        # you should allow the user to check the account balance;
        # right after creating the account, the balance should be 0.
        # It should also be possible to log out of the account and exit the program.
# Write your code here
import random
from Card import Card, is_unique, create_card, ask_info, check_valid
from user import show_and_select_main_menu, show_and_select_sub_menu

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
        card = check_valid(num, PIN, all_cards)
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
    # 0, 1, 2외의 다른 값을 입력시 다시 메뉴를 표시함.
    else:
        menu = show_and_select_main_menu() 

# 메인 메뉴에서 '0'을 선택한 경우, 프로그램 종료
print('Bye!')
exit()