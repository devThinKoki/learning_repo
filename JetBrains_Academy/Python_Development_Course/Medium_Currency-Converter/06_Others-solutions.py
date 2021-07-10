import requests

class Bank(object):
    def __init__(self):
        self.rate = {}  # keep the rate of values after processing.
        self.cache = {}  # keep the default usd and eur cache values.
        Bank.usd_eur_cache(self)  # automatically generated.

    def run(self):
        main_cur = input()
        while True:
            temp_cur = input()
            if temp_cur == '':
                return 0
            amount = float(input())
            print("Checking the cache...")
            Bank.cache_checking(self, main_cur, temp_cur, amount)

    def cache_checking(self, main_cur, cur, amount):
        cur = cur.lower()
        main_cur = main_cur.lower()
        current = ['usd', 'eur']
        # check the main and temp currency in cache dict.
        check_current_cache = (main_cur in self.cache and cur in self.cache)
        # if rate is adding the rate dict than pass or temp currency in current values and main cur not in currency
        check_current = (cur in current and main_cur not in current) or cur in self.rate
        if check_current or check_current_cache:
            print("Oh! It is in the cache!")
            if cur in current and main_cur not in current:
                #  if the temp in current, we will divide the amount the cur_rate in cache.
                given_cur_rate = float(self.cache[cur][main_cur]['rate'])
                print(f"You received {round(amount / given_cur_rate, 2)} {cur}.")
            elif cur in current and main_cur in current:
                # if the both currency in current then, we will product
                given_cur_rate = float(self.cache[main_cur][cur]['rate'])
                self.rate[cur] = given_cur_rate
                print(f"You received {round(given_cur_rate * amount, 2)} {cur.upper()}.")
            else:
                # if currency in rate dict.
                given_cur_rate = float(self.rate[cur])
                self.rate[cur] = given_cur_rate
                print(f"You received {round(given_cur_rate * amount, 2)} {cur.upper()}.")

        elif cur not in self.rate:
            # if not in the rate dict.
            print("Sorry, but it is not in the cache!")
            address = "http://www.floatrates.com/daily/"
            req = requests.get(address + main_cur + ".json")
            json_file = req.json()
            given_cur_rate = float(json_file[cur]['rate'])
            print(f"You received {round(given_cur_rate * amount, 2)} {cur.upper()}.")
            self.rate[cur] = given_cur_rate

    # Adding the cache dict for default.
    def usd_eur_cache(self):
        address = "http://www.floatrates.com/daily/"
        for i in ['usd', 'eur']:
            req = requests.get(address + i + ".json")
            json_file = req.json()
            self.cache[i] = json_file

# run the program.
def main():
    bank = Bank()
    bank.run()


if __name__ == '__main__':
    main()

################## 2 ####################
import requests
import json

cache = {}
cur_1 = input()
exc = json.loads(requests.get(f'http://www.floatrates.com/daily/{cur_1}.json').content)
if cur_1 != 'usd':
    cache['usd'] = exc['usd']['rate']
if cur_1 != 'eur':
    cache['eur'] = exc['eur']['rate']
cur_2 = input().lower()
while cur_2 != '':
    money = float(input())
    print('Checking the cache...')
    if cur_2 not in cache:
        print('Sorry, but it is not in the cache!')
        cache[cur_2] = exc[cur_2]['rate']
    else:
        print('Oh! It is in the cache!')
    print(f'You received {cache[cur_2] * money} {cur_2.upper()}.')
    cur_2 = input().lower() 


##########  3  ##########

import requests

have_currency = input().lower().strip()
wallet = {}
r = requests.get(f'http://www.floatrates.com/daily/{have_currency}.json').json()

for key in r.keys():
    if key == "usd":
        wallet['usd'] = r.get('usd')['rate']
    elif key == "eur":
        wallet['eur'] = r.get('eur')['rate']

flag = True
while flag:
    get_currency = input().lower().strip()
    if get_currency == '':
        break
    amount_money = input().strip()
    if amount_money == '':
        break
    if get_currency in wallet:
        print('Checking the cache…')
        print('Oh! It is in the cache!')
        new_currency = wallet[get_currency]
        print('You received ' + str(round(float(new_currency) * float(amount_money), 2)) + ' ' + get_currency.upper() + '.')
    else:
        print('Checking the cache…')
        print('Sorry, but it is not in the cache!')
        wallet[get_currency] = r.get(get_currency)['rate']
        new_currency = wallet[get_currency]
        print('You received ' + str(round(float(new_currency) * float(amount_money), 2)) + ' ' + get_currency.upper() + '.')


##########  4  #########
import requests
import json

class CurrencyConvertor():
    server_url = "http://www.floatrates.com/daily/{}.json"
    main_currency = ''
    cache_data = {}

    def enter_currency(self):
        self.main_currency = input()
        data = requests.get(self.server_url.format(self.main_currency))
        server_currency_info = json.loads(data.text)
        for i in ["usd", "eur"]:
            try:
                self.cache_data[i.lower()] = server_currency_info[i]
            except:
                pass

    def request_from_server(self, currency_name):
        data = requests.get(self.server_url.format(self.main_currency))
        server_currency_info = json.loads(data.text)
        self.cache_data[currency_name.lower()] = server_currency_info[currency_name.lower()]
        return self.cache_data.get(currency_name.lower())['rate']

    def exchange_currency_name(self, name, amount):
        print("Checking the cache...")
        if self.cache_data.get(name.lower(), False):
            print("Oh! It is in the cache!")
            rate = self.cache_data.get(name.lower())['rate']
        else:
            print("Sorry, but it is not in the cache!")
            rate = self.request_from_server(name)
        print("You received {} USD.".format(round(amount * rate, 2)))

    def start(self):
        self.enter_currency()
        while True:
            name = input()
            if name == "":
                break
            amount = float(input())
            self.exchange_currency_name(name, amount)
CurrencyConvertor().start()