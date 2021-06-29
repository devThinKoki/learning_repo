# Description
    # It's very upsetting when the data about registered users disappears after the program is completed. 
    # To avoid this problem, you need to create a database where you will store all the necessary information about the created credit cards. 
    # We will use SQLite to create the database.

    # SQLite is a database engine. 
    # It is a software that allows users to interact with a relational database. 
    # In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines. 
    # This allows for greater accessibility: 
        # copying a database is no more complicated than copying the file that stores the data, and sharing a database implies just sending an email attachment.

    # You can use the "sqlite3" module to manage SQLite database from Python. 
    # You don't need to install this module. 
    # It is included in the standard library.

    # To use the module, you must first create a "Connection" object that represents the database. 
    # Here the data will be stored in the example.s3db file:
        # import sqlite3
        # conn = sqlite3.connect('example.s3db')
    
    # Once you have a Connection, you can create a "Cursor" object and call its "execute()"" method to perform SQL queries:
            # # Create a Cursor object
            # cur = conn.cursor()

            # # Executes some SQL query
            # cur.execute('SOME SQL QUERY')

            # # After doing some changes in DB don't forget to commit them!
            # conn.commit()

    # To get data returned by "SELECT" query you can use fetchone(), fetchall() methods:
            # cur.execute('SOME SELECT QUERY')

            # # Returns the first row from the response
            # cur.fetchone()

            # # Returns all rows from the response
            # cur.fetchall()
 
# Objectives
    # In this stage, create a database named "card.s3db" with a table titled "card". 
    # It should have the following columns:
        # id INTEGER
        # number TEXT
        # pin TEXT
        # balance INTEGER DEFAULT 0

    # Pay attention: 
        # your database file should be created when the program starts if it hasn’t yet been created. 
        # And all created cards should be stored in the database from now.

    # Do not forget to commit your DB changes right after executing a query!


######################  main part  ###################
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
                    print(f'Balance: {card[3]}')
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
    # if user choose '0: Exit' program will close()
    elif menu == '0':
        print('Bye!')
        exit()
    else:
    # if user give value as input() not among '0', '1' nor '2', display menu again
        menu = show_and_select_main_menu() 