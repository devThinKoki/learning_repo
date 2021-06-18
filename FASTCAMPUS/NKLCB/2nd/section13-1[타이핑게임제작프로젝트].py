# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본완성

import random
import time

words = []                                              # 영어 단어 리스트(1000개의 단어 로드)

n = 1                                                   # 게임 시도 횟수 변수
cor_cnt = 0                                             # 맞힌 문제 갯수 변수

with open('./2nd/sec13_resource/word.txt', 'r') as f:   # 문제가 담긴 txt 파일을 f라는 이름으로 로드
    for c in f:                                         # 파일 안의 각각의 줄에 대하여,
        words.append(c.strip())                         # words 리스트에 양쪽 공백을 제거하여 삽입
# print(words)                                            # 단어 리스트 확인


a = input("Ready? Press Enter Key!")                    # Enter키를 눌러 게임 시작을 유도

start = time.time()                                     # 게임 시작한 시점의 시간을 저장

while n <= 5:                                           # 총 5회 단어 따라적기를 테스팅 할 예정
    random.shuffle(words)                               # words 리스트 안의 요소를 shuffle()로 섞어 준다.
    question = random.choice(words)                     # words 리스트에서 무작위로 하나를 뽑아 변수에 저장
    print()

    print("Question # {}: ".format(n))
    print(question)

    user_input = input()
    print()

    if str(question).strip() == str(user_input).strip():# 유저가 입력한 값과 주어진 문제의 값이 같을 경우,
        print('Pass!')
        cor_cnt += 1
    else:
        print('Wrong!')
    n += 1
end =  time.time()                                      # 5문제를 다 풀었을 때의 시간
Total_time = end - start                                # 총시간을 계산(끝난 시간 - 시작 시간)
Total_time = format(Total_time, ".3f")                  # 시간이 소수점자리수가 길기 때문에, 소수단위 3자리 까지의 float 타입으로 지정
print()

if cor_cnt >= 3:
    print('합격!')
else:
    print('불합격!')

# 수행 시간 출력
print("게임시간 : ", Total_time, "초 ", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == "__main__":
    pass


# words = []                                   # 영어 단어 리스트(1000개 로드)

# n = 1                                        # 게임 시도 횟수
# cor_cnt = 0                                  # 정답 개수

# with open('./resource/word.txt', 'r') as f:  # 문제 txt 파일 로드
#     for c in f:
#         words.append(c.strip())

# print(words)                                 # 단어 리스트 확인

# input("Ready? Press Enter Key!")             # Enter Game Start!

# start = time.time()                          # Start Time

# while n <= 5:                                # 5회 반복
#     random.shuffle(words)                    # List shuffle!
#     q = random.choice(words)                 # List -> words random extract!

# 	print()

#     print("*Question # {}".format(n))
#     print(q)                                 # 문제 출력

#     x = input()                              # 타이핑 입력

# 	print()
    
#     if str(q).strip() == str(x).strip():     # 입력 확인(공백제거)
#         print("Pass!")
#         cor_cnt += 1                         # 정답 개수 카운트
#     else:
#         print("Wrong!")

#     n += 1                                   # 다음 문제 전환

# end = time.time()                            # End Time
# et = end - start                             # 총 게임 시간

# et = format(et, ".3f")                       # 소수 셋째 자리 출력(시간)

# if cor_cnt >= 3:                             # 3개 이상 합격
#     print("결과 : 합격")
# else:
#     print("불합격")
    
# # 수행 시간 출력
# print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

# # 시작지점
# if __name__ == '__main__':
#     pass
