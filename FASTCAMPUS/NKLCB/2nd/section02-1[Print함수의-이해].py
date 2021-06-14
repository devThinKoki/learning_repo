# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print('using -> \' <- in print() is allowed')
print("using -> \" <- in print() is allowed")
print('''using -> \'\'\' <- in print() is allowed''')
print("""using -> \"\"\" <- in print() is allowed""")
print()
print('if you don\'t give any parameter to print().\n\tyou can see an empty line added above')
print()

print('-'*10, 'Seperator 옵션 사용', '-'*10)
print(r"print('T', 'E', 'S', 'T'): ", end='')
print('T', 'E', 'S', 'T')
print(r"print('T', 'E', 'S', 'T', sep=''): ", end='')
print('T', 'E', 'S', 'T', sep='')
print(r"print('T', 'E', 'S', 'T', sep='-'): ", end='')
print('T', 'E', 'S', 'T', sep='-')
print(r"print('niceman', 'google.com', sep='@'): ", end='')
print('niceman', 'google.com', sep='@')

print('-'*10, 'end 옵션 사용', '-'*10)
print(r"""print('Welcome To', end='')
print('the black parade', end=' ')
print('piano notes')
print('this line will be new line')
""")
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
print('this line will be new line')

print('-'*10,'format함수 사용 [], {}, ()', '-'*10)
print('{} and {}'.format('You', 'Me'))
# {}안에 아무것도 적지 않으면, format()의 인자값을 순서대로 사용하고,
print("{0} and {1} and {0}".format('You', 'Me'))
# {}안에 0부터 숫자가 들어가면, format()의 인자값을 인덱스 순서대로 사용한다. 
print('{a} are {b}'.format(b='Me', a='You'))
# format의 인자값으로 키와 값을 전달하면, 문자열에서 해당 키를 사용하여 값을 사용할 수 있다.

print("%s: 문자, %d: 정수, %f: 실수")
print("%s's favorite number is %d" %('Eunki', 7))
# %s를 사용하면, 문자가 올것을 암시, %d를 사용하는 곳에는 숫자가 옴을 암시할 수 있다.
print("Test1: %5d, Price: %4.2f" % (776, 6543.123))
print("Test2: {0: 5d}, Price:{1: 4.2f}".format(776,6543.123))
print("Test3: {a: 5d}, Price:{b: 4.2f}".format(b=6543.123, a=776))