import json
import requests

country = input()
# print(country.lower())
url = f"http://www.floatrates.com/daily/{country.lower()}.json"
r = requests.get(url)
json_dict = r.text
# print(type(json_dict))
py_dict = json.loads(json_dict)
# print(type(py_dict))
print(py_dict['usd'])
print(py_dict['eur'])