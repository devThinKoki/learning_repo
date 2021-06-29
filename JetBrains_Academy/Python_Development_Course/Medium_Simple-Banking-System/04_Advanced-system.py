# Description
    # You have created the foundation of our banking system. 
    # Now let's take the opportunity to deposit money into an account, make transfers and close an account if necessary.

    # Now your menu should look like this:
        # 1. Balance
        # 2. Add income
        # 3. Do transfer
        # 4. Close account
        # 5. Log out
        # 0. Exit

    # "Balance", you should read the balance of the account from the database and output it into the console.

    # "Add income" should allow us to deposit money to the account.

    # "Do transfer" should allow transferring money to another account. 
    # You should handle the following errors:
        # If the user tries to transfer more money than he/she has, output: Not enough money!
        # If the user tries to transfer money to the same account, output the following message: You can't transfer money to the same account!
        # If the receiver's card number doesn’t pass the Luhn algorithm, you should output: Probably you made a mistake in the card number. Please try again!
        # If the receiver's card number doesn’t exist, you should output: Such a card does not exist.
        # If there is no error, ask the user how much money they want to transfer and make the transaction.
        # If the user chooses the Close account item, you should delete that account from the database.

# Do not forget to commit your DB changes right after executing a query!

from db import *
from user import *
from Card import *
# create initial db
createTable()
menu = show_and_select_main_menu()
# function: to show main menu options and let user to select one of them
while True:
    # case1: if user choose '1' from main menu option
    if menu == '1':
        # create new Card object
        new_card = Card()
        # 기존에 있던 카드와 정보가 일치 하지 않으면(고유한 카드이면)
        if is_unique(new_card):
            # 카드 객체 생성 후, 카드 객체 배열에 추가
            create_insert_card(new_card)
        menu = show_and_select_main_menu()
    
    elif menu == '2':
        # ask user about the num and pin
        num, pin = ask_info()
        # check if card with given info(num, pin) exist
        card = check_valid(num, pin)
        if card:
            print('You have successfully logged in!')
            print()
            # if exist show sub_menu and let user select one of the option
            sub_menu = show_and_select_sub_menu()
            while True:
                # case 2-1: print balance of the card(object) from card db
                if sub_menu == '1':
                    show_balance(card[1], card[2])
                # case 2-2(Add income): 
                elif sub_menu == '2':
                    income = input('Enter income:\n')
                    try:
                        income = int(income)
                    except:
                        exit()
                    add_income(income, card[1], card[2])
                # case 2-3(Do transfer): 
                elif sub_menu == '3':
                    to_account_num = input('Transer\nEnter card number:\n')
                    try_transfer(to_account_num, card)

                # case 2-4(Close account): 
                elif sub_menu == '4':
                    delete_account(card)

                # case 2-5(Log out): 서브 메뉴 while문 탈출하며, 메인 메뉴 선택화면으로 변경
                elif sub_menu == '5':
                    print('You have successfully logged out!')
                    print()
                    menu = show_and_select_main_menu()
                    break
                # case 2-0(Exit): exit the program
                elif sub_menu == '0':
                    print('Bye!')
                    exit()
                sub_menu = show_and_select_sub_menu()
        # card에 Card객체가 담기지 않았다면(정보불일치),
        # 메인 메뉴 선택 화면으로 이동
        else:
            print('Wrong card number or PIN!')
            print()
            menu = show_and_select_main_menu()
    # if user choose '0: Exit' program will close()
    elif menu == '0':
        print('Bye!')
        exit()
    else:
    # if user give value as input() not among '0', '1' nor '2', display menu again
        menu = show_and_select_main_menu() 