# 메인메뉴를 출력하고, 입력을 받아 사용자가 선택한 메뉴의 번호를 반환하는 함수 생성
def show_and_select_main_menu():
    print('1. Create an account\n2. Log into account\n0. Exit')
    menu = input()
    print()
    return menu

def show_and_select_sub_menu():
    print('1. Balance\n2. Log out\n0. Exit')
    sub_menu = input()
    print()
    return sub_menu