import random

def initial_start():
    print('Please give AI some data to learn...')
    data_list = []
    while True:
        print(f'The current data length is {len(data_list)}, {100 - len(data_list)} symbols left')
        print('Print a random string containing 0 or 1:\n')
        user = input()
        for num in [n for n in user if n == '0' or n == '1']:
            data_list.append(num)
        if len(data_list) >= 100:
            break
    final_str = ''.join(data_list)
    print(f"\nFinal data string:\n{final_str}\n")
    return final_str


def statistics(final_str):
    bin_li = {str(i) + str(j) + str(k):[0,0] for i in range(2) for j in range(2) for k in range(2)}
    for bin in bin_li.keys():
        idx = -1
        while  idx < len(final_str) - 4:
            temp_idx = final_str.find(bin, idx + 1)
            if temp_idx == -1 or temp_idx == len(final_str) - 3:
                break
            if final_str[temp_idx + 3] == '0':
                bin_li[bin][0] += 1
            else:
                bin_li[bin][1] += 1
            idx = temp_idx
    return bin_li


def predict(bin_li):
    capital = 1000
    print(f"""You have ${capital}. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")
    while True:
        triads = {str(i) + str(j) + str(k):[0,0] for i in range(2) for j in range(2) for k in range(2)}
        print("\nPrint a random string containing 0 or 1:")
        user_str = input()
        if user_str == 'enough':
            print('Game over!')
            break

        preprocessed_str = [c for c in user_str if c == '1' or c == '0']
        if len(preprocessed_str) == 0:
            continue
        
        predicted_str = [str(random.choice([0, 1])) for i in range(3)]

        for i in range(3, len(user_str)):
            triad = ''.join(user_str[i - 3:i])
            if bin_li[triad][0] > bin_li[triad][1]:
                predicted_str.append('0')
                triads[triad][0] += 1
            elif bin_li[triad][1] > bin_li[triad][0]:
                predicted_str.append('1')
                triads[triad][1] += 1
            else:
                randomchoice = random.choice(['0', '1'])
                predicted_str.append(randomchoice)
                triads[triad][int(randomchoice)] += 1
        capital = calculate_accuracy(user_str, predicted_str, capital)
        for tr, li in triads.items():
            bin_li[tr][0] += li[0]
            bin_li[tr][1] += li[1]
        # print(bin_li)
    return user_str, ''.join(predicted_str)


def calculate_accuracy(user, predicted_str, capital):
    correct, total = 0, len(user) - 3
    for i, c in enumerate(user):
        if i < 3:
            continue
        if c == predicted_str[i]:
            correct += 1
    capital = capital + total - correct - correct
    acc = round(correct / total * 100, 2)
    print(f"prediction:\n{''.join(predicted_str)}")
    print(f"\nComputer guessed right {correct} out of {total} symbols ({acc} %)")
    print(f'Your capital is now ${capital}')
    return capital

final_s = initial_start()
bins = statistics(final_s)
# print(bins)
user, predicted = predict(bins)

# calculate_accuracy(user, predicted)