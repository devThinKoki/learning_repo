data_list = []
while True:
    print('Print a random string containing 0 or 1:\n')
    user = input()
    for num in [n for n in user if n == '0' or n == '1']:
        data_list.append(num)
    if len(data_list) >= 100:
        break
    print(f'Current data length is {len(data_list)}, {100 - len(data_list)} symbols left')
print()
print(f"Final data string:\n{''.join(data_list)}")

# 000: 0,3
# 001: 10,5
# 010: 13,18
# 011: 5,2
# 100: 3,12
# 101: 20,3
# 110: 2,5
# 111: 2,1