# show and select main menu and return user input
def show_and_select_main_menu():
    print('1. Create an account\n2. Log into account\n0. Exit')
    menu = input()
    print()
    return menu

# show and select_sub menu and return user input
def show_and_select_sub_menu():
    print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
''')
    sub_menu = input()
    print()
    return sub_menu
