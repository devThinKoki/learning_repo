def init():
    score1, score2, score3 = int(input()), int(input()), int(input())
    mean = calculate_mean(score1, score2, score3)
    print_result_msg(mean)

def calculate_mean(*args):
    return sum(args) / len(args)

def print_result_msg(m):
    print(m)
    if m >= 60.0:
        print("Congratulations, you are accepted!")
    elif m < 60.0:
        print('We regret to inform you that we will not be able to offer you admission.')

init()