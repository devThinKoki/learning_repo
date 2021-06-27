import random
# Card 객체 생성하기 위한 클래스
class Card:
    def __init__(self, num = None, PIN = None, bal = 0): 
        if num:
            self.num = num
        else:
            self.num = str(random.randrange(4000000000000000,4000010000000000))
        if PIN:
            self.PIN = PIN
        else:
            self.PIN = ''.join([str(random.randint(0,9)) for _ in range(4)])
            # self.PIN = format(random.randint(0000,9999), '04d')
        self.bal = bal
    
    def get_info(self):
        print(f'Card-num: {self.num}, Card-PIN: {self.PIN}')

# '새롭게 생성한 new_card(객체)의 카드번호'가 '배열(all_cards)속 Card객체들의 번호'와 다른가?
def is_unique(new_card, all_cards):
    for card in all_cards:
        if new_card.num == card.num:
            return False
    return True

# 객체(new_card)가 생성 성공 메세지를 출력하고, Card객체들이 담긴 배열(all_card)에 추가하기
def create_card(new_card, all_cards):
    print("Your card has been created")
    print("Your card number:")
    print(new_card.num)
    print("Your card PIN:")
    print(new_card.PIN)
    all_cards.append(new_card)
    print()

# 사용자에게 Card객체에 대한 정보(num, PIN)을 요구하고 이를 반환하기
def ask_info():
    print('Enter your card number:')
    num = input()
    print('Enter your PIN:')
    PIN = input()
    print()
    return num, PIN

def check_valid(num, PIN, all_cards):
    for card in all_cards:
        if card.num == num and card.PIN == PIN:
            return card
    return None

# import가 아닌 해당 파일에서 디버깅시에만 실행되는 코드
if __name__ == '__main__':
    for i in range(1000):
        card = Card()
        card.get_info()