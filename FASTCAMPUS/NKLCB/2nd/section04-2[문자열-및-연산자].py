
print('-'*10,'문자열 함수','-'*10)
# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

a = 'niceman'
b = 'orange'
print('a = nice man')
print('b = orange')
print(r'print(a.islower()):', a.islower())  # 소문자로 이뤄진 문자열인가? T/F
print(r"print(b.endswith('e')):", b.endswith('e')) # 인자값으로 문자열이 끝나는가? T/F
print(r'print(a.capitalize()):', a.capitalize()) # 문자열의 첫문자를 대문자화
print(r"print(a.replace('nice', 'good')):", a.replace('nice', 'good')) # 문자열에서 첫번째 인자값인 인덱스 위치로 부터 해당 문자들을 두번째 인자값으로 변경
print(r'print(list(reversed(b)):', list(reversed(b))) # 문자열을 reversed(역순)으로 배열한 뒤, 각각의 문자를 원소로 갖는 리스트로 생성


print('-'*10,'슬라이싱','-'*10)
print('a = nice man')
print('b = orange')
print(r'print(a[:3])', a[:3]) # print(a[0:3]) 과 같다. 0번째 인덱스요소부터 3-1 번째 요소까지를 출력
print(r'print(a[:4])',a[:4])
print(r'print(a[:len(a)]:', a[:len(a)])
print(r'print(a[:]:',a[:])
print(r'print(b[0:4:2]:',b[0:4:2]) # 첫번째 인덱스 요소부터 두번째값-1 번째 인덱스 요소까지 세번째인자값만큼 뛰어넘으며 출력
print(r'print(b[1:-2]:',b[1:-2])
print(r'print(b[::-1]:',b[::-1]) #처음부터 끝까지의 요소들을 뒤에서부터 거꾸로 출력 [print(reversed(문자열))의 결과와 같다.]