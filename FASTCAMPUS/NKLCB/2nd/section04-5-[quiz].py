# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print("1. ", len(q1))
# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("2. ", """apple;orange;banana;lemon""")

# 3. 화면에 * 기호 100개를 표시하세요.
print("3. ", '*'*100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
print("4. ", int("30"), float("30"), complex("30"), str(30))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
q5 = "Niceman"
q5_idx = q5.index('man')
print("5. ", q5[4:7])
print("\t", "q5_idx: ", q5_idx)
print("\t", q5[q5_idx:q5_idx+3])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
q6 = "Strawberry"
# print("6. ", list(reversed(q6)))
print("6. ", q6[::-1])

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
q7 = "010-7777-9999"
print("7. ", q7[:3]+q7[4:8]+q7[9:])
print("7. ", q7.replace("-",""))
# 정규표현식으로 풀어보기
import re
print("7. ", re.sub('[^0-9]','',q7)) # sub()은 ^(아니다)0-9 가 아닌 문자들을 ''로 대체하여 결과를 반환

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
q8 = 'http://daum.net'
print("8. ", q8[7:])
print("8. ", q8.replace('http://',''))
print("8. ", re.sub('http://','',q8))

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
q9 = "Niceman"
print("9. ", q9.upper())
print("9. ", q9.lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
q10 = "abcdefghijklmn"
q10_idx = q10.index("cde")
print("10. ", q10[2:5])
print("10. ", q10[q10_idx:q10_idx+3])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
q11 = ["Banana", "Apple", "Orange"]
q11.remove("Apple")
print("11. ", q11)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
q12_tup = (1,2,3,4)
q12_list = list(q12_tup)
print("12. ", q12_list)
print([s for s in q12_tup])

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
q13 = {"성인": 100000, "청소년": 70000, "아동": 30000}
print("13. ", q13)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
q13["소아"] = 0
print("14. ", q13)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print("15. ", list(q13.keys()))

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print("16. ", list(q13.values()))

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***