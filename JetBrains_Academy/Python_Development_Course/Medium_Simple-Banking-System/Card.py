import random
# function: algorithm to return card number with valid check_sum
def luhn_Algorithm():
    digits = list(format(random.randint(400000000000000,400000999999999), '015d'))
    sum = 0
    for idx, num in enumerate(digits):
        # for number which located in odd index(idx + 1) multiply it by 2.
        if idx % 2 == 0:
            if int(num) >= 5:
                # which is greater than 9 after multiply opertaion, do -9 opertion.
                sum += int(num) * 2 - 9
            else:
                sum += int(num) * 2
        else:
            sum += int(num)
    if sum % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - (sum % 10)
    digits.append(str(last_digit))
    return ''.join(digits)

# # class code for create Card Object
class Card:
    def __init__(self):
        self.num = luhn_Algorithm()
        self.PIN = format(random.randint(0000,9999), '04d')
        self.bal = 0

def test_luhn(account_num):
    if len(account_num) != 16:
        return False
    digits = list(account_num)
    sum = 0
    for idx, num in enumerate(digits):
        if idx == len(digits)-1 :
            sum += int(num)
        elif idx % 2 == 0:
            if int(num) >= 5:
                sum += int(num) * 2 - 9
            else:
                sum += int(num) * 2
        else:
            sum += int(num)
    return sum % 10 == 0

# ask user for card-num and card-PIN and return them
def ask_info():
    num = input('Enter your card number:\n')
    if len(num) != 16:
        return exit()
    pin = input('Enter your PIN:\n')
    print()
    return num, pin
