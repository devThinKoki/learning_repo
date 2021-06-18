def foo(s):
    print('wow') # 설마... 이렇게 그냥 'wow'문자열을 출력하면 되는 것일까??
    # 왜냐하면 아래의 코드 상에서는 s가 전역변수가 아닌 이상 UnboundLocalError가 발생할 일이 없다.
    try:
        s += '1'
    except UnboundLocalError:
        print('wow')
    except:
        print('owo')
    
foo('abc')
# 기대 출력값
# 'wow'
