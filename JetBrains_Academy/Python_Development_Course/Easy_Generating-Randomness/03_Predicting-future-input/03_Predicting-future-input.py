import random

def initial_start():
    data_list = []
    while True:
        print('Print a random string containing 0 or 1:\n')
        user = input()
        for num in [n for n in user if n == '0' or n == '1']:
            data_list.append(num)
        if len(data_list) >= 100:
            break
        print(f'Current data length is {len(data_list)}, {100 - len(data_list)} symbols left')
    final_str = ''.join(data_list)
    print(f"\nFinal data string:\n{final_str}\n")
    return final_str

def statistics(final_str):
    bins = {str(i) + str(j) + str(k):[0,0] for i in range(2) for j in range(2) for k in range(2)}
    for bin in bins.keys():
        idx = -1
        while  idx < len(final_str) - 4:
            temp_idx = final_str.find(bin, idx + 1)
            if temp_idx == -1 or temp_idx == len(final_str) - 3:
                break
            if final_str[temp_idx + 3] == '0':
                bins[bin][0] += 1
            else:
                bins[bin][1] += 1
            idx = temp_idx
        # print(f"{bin}: {bins[bin][0]},{bins[bin][1]}")
    return bins

def predict(bins):
    print("\nPlease enter a test string containing 0 or 1:\n")
    user = input()
    
    predicted_str = [str(random.choice([0, 1])) for i in range(3)]
    for i in range(len(user) - 3):
        triad = ''.join(predicted_str[i:i + 3])
        if bins[triad][0] > bins[triad][1]:
            predicted_str.append('0')
            bins[triad][0] += 1
        elif bins[triad][1] > bins[triad][0]:
            predicted_str.append('1')
            bins[triad][1] += 1
        else:
            predicted_str.append(random.choice(['0','1']))
    return user, ''.join(predicted_str)

def calculate_accuracy(user, predicted_str):
    Correct, Total = 0, len(user) - 3
    for i, c in enumerate(user):
        if i < 3:
            continue
        if c == predicted_str[i]:
            Correct += 1
    ACC = round(Correct / Total * 100, 2)
    print(f"prediction:\n{predicted_str}")
    print(f"\nComputer guessed right {Correct} out of {Total} symbols ({ACC} %)")

final_str = initial_start()
bins = statistics(final_str)
user, predicetd_str = predict(bins)
calculate_accuracy(user,predicetd_str)

#### Use below function if you want to write one-line function call but not so readable.
# def calculate_accuracy(tup):
#     user, predicted_str = tup[0], tup[1]
#     Correct, Total = 0, len(user) - 3
#     for i, c in enumerate(user):
#         if i < 3:
#             continue
#         if c == predicted_str[i]:
#             Correct += 1
#     ACC = round(Correct / Total * 100, 2)
#     print(f"prediction:\n{predicted_str}")
#     print(f"\nComputer guessed right {Correct} out of {Total} symbols ({ACC} %)")

# calculate_accuracy(predict(statistics(initial_start())))