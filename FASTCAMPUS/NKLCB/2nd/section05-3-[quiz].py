# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
from typing import Literal


q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k in q1.keys():
    if k == '가을':
        print(q1[k])
        break

for k, v in q1.items():
    if k == '가을':
        print(v)
        break

print(''.join([q1[s] for s in q1 if s == '가을']))

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k, v in q2.items():
    if k == '사과' or v == '사과':
        print(k,": ", v)
        break
else:
    print('사과 없음')

hasApple = ['사과다!!' for k,v in q2.items() if k == '사과' or v == '사과']
if len(hasApple):
    print('사과 있음')
else:
    print('사과 없음')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 24
if score >= 81:
    print('A학점')
elif score >= 61:
    print('B학점')
elif score >= 41:
    print('C학점')
elif score >= 21:
    print('D학점')
else:
    print('E학점')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18
max_value = a
if b > a:
    max_value = b
if c > b:
    max_value = c
print(max_value)

print(max(list([a,b,c])))

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-3473837'
if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정", '무', '기']
for c in q3:
    if c == '정':
        continue
    print(c, end =' ')
print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1,101):
    if i % 2 == 1:
        print(i, end = ' ')
print()

print(' '.join([str(i) for i in range(1,100) if i % 2 == 1]))

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for c in q4:
    if len(c) >= 5:
        print(c, end= ' ')
print()

print(' '.join([s for s in q4 if len(s)>=5]))
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for c in q5:
    if c.isupper():
        continue
    print(c, end = ' ')
print()
print(' '.join([c for c in q5 if c.islower()]))


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for c in q6:
    if c.islower():
        print(c.upper(), end = ' ')
    else:
        print(c.lower(), end = ' ')
print()
print(' '.join([c.lower() if c.isupper() else c.upper() for c in q6]))