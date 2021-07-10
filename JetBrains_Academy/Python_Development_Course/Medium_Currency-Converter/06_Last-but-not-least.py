import json
import requests
cache = {}

def return_pydict(country):
    global cache
    # get the json URL with your country(curreny) code
    url = f"http://www.floatrates.com/daily/{country.lower()}.json"
    r = requests.get(url)
    json_dict = r.text # type is text
    py_dict = json.loads(json_dict) # type is dict
    return py_dict

def caching(country):
    global cache, py_dict
    cache[country] = {}
    if country != 'usd':
        cache[country]['usd'] = float(py_dict['usd']['rate'])
    if country != 'eur':
        cache[country]['eur'] = float(py_dict['eur']['rate'])
# Take the currency code which you want to exchange from.
country = input()
if not country:
    exit()
country = country.lower()
py_dict = return_pydict(country)
caching(country.lower())
    
while True:
    # Take the currency code which you want to receive as.
    to_country = input().lower()
    if not to_country:
        break
    # Take the amount of money you have.
    amount = float(input())
    print('Checking the cache...')
    if to_country in cache[country].keys():
        print('Oh! It is in the cache!')
        received = amount * cache[country][to_country]
        formatted_received = "{:.2f}".format(received)
        print(f"You received {formatted_received} {to_country.upper()}.")
        continue
    print('Sorry, but it is not in the cache!')
    cache[country][to_country] = float(py_dict[to_country]['rate'])
    received = amount * cache[country][to_country]
    formatted_received = "{:.2f}".format(received)
    print(f"You received {formatted_received} {to_country.upper()}.")

# # get the json URL with your country(curreny) code
# url = f"http://www.floatrates.com/daily/{country.lower()}.json"
# r = requests.get(url)
# json_dict = r.text # type is text
# py_dict = json.loads(json_dict) # type is dict

# cache[country] = {}
# cache[country]['usd'] = float(py_dict['usd']['rate'])
# cache[country]['eur'] = float(py_dict['eur']['rate'])