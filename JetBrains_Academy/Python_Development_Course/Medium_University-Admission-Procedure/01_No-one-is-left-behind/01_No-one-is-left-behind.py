def init():
    score1, score2, score3 = int(input()), int(input()), int(input())
    mean = calculate_mean(score1, score2, score3)
    print(mean)
    print("Congratulations, you are accepted!")

def calculate_mean(*args):
    return sum(args) / len(args)

init()