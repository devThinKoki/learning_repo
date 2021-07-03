# print("의문: 리스트 변수는 언제 주소가 바뀌는가?")
# print("\t원본리스트, 객체참조, [:]복사, copy복사, deepcopy롤 각각 리스트 복사완료")
# import copy
# li_ori = [1,2,3,4,5]
# li1 = li_ori
# li2 = li_ori[:]
# li3 = copy.copy(li_ori)
# li4 = copy.deepcopy(li_ori)
# print()
# print('EX01-')
# print("="*22, "각 리스트의 아이디 출력", "="*22)
# print('   ', "li_ori", '  |    ', 'li1', '    |   ', 'li2', '     |   ', 'li3', '     |    ', 'li4', '   ')
# print(id(li_ori), id(li1), id(li2), id(li3), id(li4), sep='|')

# print()
# print('EX02-')
# print("="*22, "원본 리스트에 함수 적용", "="*22)
# print('li_ori.append(1) 실행')
# li_ori.append(1)
# print('   ', "li_ori", '  |    ', 'li1', '    |   ', 'li2', '     |   ', 'li3', '     |    ', 'li4', '   ')
# print(li_ori, li1, li2, li3, li4, sep = ' ')
# print(id(li_ori), id(li1), id(li2), id(li3), id(li4), sep = '|')


# print()
# print('EX03-')
# print("="*22, "원본 리스트의 값을 변경", "="*22)
# print('li_ori[0] = 0 실행')
# li_ori[0] = 0
# print('   ', "li_ori", '  |    ', 'li1', '    |   ', 'li2', '     |   ', 'li3', '     |    ', 'li4', '   ')
# print(li_ori, li1, li2, li3, li4, sep = ' ')
# print(id(li_ori), id(li1), id(li2), id(li3), id(li4), sep='|')

priority_pieces = {i : 0 for i in range(7)}
print(priority_pieces)
priority_pieces[3] += 9
print(priority_pieces)
print(max(priority_pieces.keys(), key = lambda x: priority_pieces[x]))


def computer_move():
    global stock_pieces, computer_pieces, domino_pieces
    input('Computer is about to make a move. Press Enter to continue...\n')
    negative_min = 0 - len(computer_pieces)
    positive_max = len(computer_pieces)

    while True:
        random_number = random.randint(negative_min, positive_max)
        if random_number == 0:
            if not stock_pieces:
                return 'draw'
            stock_pieces, popped_piece = pop_from_stock(stock_pieces)
            computer_pieces.append(popped_piece)
            break
        if is_violate_rule(computer_pieces, domino_pieces, random_number):
            continue

        popped_piece = pop_from_pieces('computer', random_number)
        update_number_cnt(popped_piece)
        if random_number < 0:
            domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, -1)
            break
        else:
            domino_pieces = place_to_domino_snake(domino_pieces, popped_piece, 1)
            break