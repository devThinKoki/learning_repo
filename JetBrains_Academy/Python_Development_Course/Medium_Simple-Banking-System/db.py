import sqlite3
from Card import test_luhn

def createTable():
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = '''CREATE TABLE IF NOT EXISTS card
(id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);
'''
    cur.execute(SQL_QUERY)
    conn.commit()
    conn.close()

# check whether newly created card's info is exist in db
def is_unique(new_card):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = f"SELECT * FROM card WHERE number = {new_card.num} and pin = {new_card.PIN}"
    cur.execute(SQL_QUERY)
    card = cur.fetchone()
    conn.commit()
    conn.close()
    if not card:
        return True
    elif new_card.num == card[1] and new_card.PIN == card[2]:
        return False
    return True

# print some infor about new_card(object) insert it to card(database)
def create_insert_card(new_card):
    print("Your card has been created")
    print("Your card number:")
    print(new_card.num)
    print("Your card PIN:")
    print(new_card.PIN)
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute('INSERT INTO card (number, pin) VALUES (?,?)', (new_card.num, new_card.PIN))
    conn.commit()
    conn.close()
    print()

# for given num and PIN, return if there is Card object which has same num and PIN attribute value,
def check_valid(num, pin):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = f'SELECT * FROM card WHERE number={num} AND pin={pin}'
    cur.execute(SQL_QUERY)
    card = cur.fetchone()
    conn.commit()
    conn.close()
    if card:
        return card
    return False

def show_balance(num, pin):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = f'SELECT * FROM card WHERE number = {num} AND pin = {pin}'
    cur.execute(SQL_QUERY)
    card = cur.fetchone()
    conn.commit()
    conn.close()
    print(f'Balance: {card[3]}')
    print()

def add_income(income, num, pin):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = f'UPDATE card SET balance = balance + {income} WHERE number = {num} AND pin = {pin}'
    cur.execute(SQL_QUERY)
    conn.commit()
    conn.close()
    print('Income was added!')
    print()

def if_exist(to_account_num):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = f"SELECT * FROM card WHERE number = {to_account_num}"
    cur.execute(SQL_QUERY)
    card = cur.fetchone()
    conn.commit()
    conn.close()
    if not card:
        return False
    if to_account_num == card[1]:
        return card
    return False

def try_transfer(to_account_num, user_card):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = f"SELECT * FROM card WHERE number = {user_card[1]}"
    cur.execute(SQL_QUERY)
    user_card = cur.fetchone()
    conn.commit()
    conn.close()
    to_account_card = if_exist(to_account_num)

    # If the user tries to transfer money to the same account, output the following message: You can't transfer money to the same account!
    if to_account_num == user_card[1]:
        print("You can't transfer money to the same account!")

    # If the receiver's card number doesn’t pass the Luhn algorithm, you should output: Probably you made a mistake in the card number. Please try again!
    elif not test_luhn(to_account_num):
        print("Probably you made a mistake in the card number. Please try again!")

    # If the receiver's card number doesn’t exist, you should output: Such a card does not exist.
    elif not to_account_card:
        print("Such a card does not exist")

    # If there is no error, ask the user how much money they want to transfer and make the transaction.
    else:
        amount = input('Enter how much money you want to transfer:\n')
        try:
            amount = int(amount)
        except:
            print('not integer given')
            exit()
        # If the user tries to transfer more money than he/she has, output: Not enough money!
        if amount > user_card[3]:
            print('Not enough money!')
        else:
            do_transfer(amount, user_card, to_account_card)
    print()
    return

def do_transfer(amount, user_card, to_account_card):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL1 = f'UPDATE card SET balance = balance - {amount} WHERE number = {user_card[1]}'
    SQL2 = f'UPDATE card SET balance = balance + {amount} WHERE number = {to_account_card[1]}'
    cur.execute(SQL1)
    cur.execute(SQL2)
    conn.commit()
    conn.close()
    print('Success!')
    return

# If the user chooses the Close account item, you should delete that account from the database.
def delete_account(card):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    SQL_QUERY = f'DELETE FROM card WHERE number = {card[1]}'
    cur.execute(SQL_QUERY)
    conn.commit()
    conn.close()
    print('The acccount has been closed!')
    print()
    return