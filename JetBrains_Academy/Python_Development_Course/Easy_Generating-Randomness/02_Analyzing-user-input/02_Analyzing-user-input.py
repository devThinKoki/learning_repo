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
final_str = ''.join(data_list)
print(f"Final data string:\n{final_str}")

bins = [str(i) + str(j) + str(k) for i in range(2) for j in range(2) for k in range(2)]
for i in range(len(bins)):
    cnt_0, cnt_1, idx = 0, 0, -1
    while  idx < len(final_str) - 4:
        temp_idx = final_str.find(bins[i], idx + 1)
        if temp_idx == -1:
            break
        if temp_idx == len(final_str) - 3:
            break
        if final_str[temp_idx + 3] == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
        idx = temp_idx
    print(f"{bins[i]}: {cnt_0},{cnt_1}")