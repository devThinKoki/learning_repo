class Stack:
    def __init__(self):
        # 여기에 코드 작성
        self.top = -1
        self.arr = [False for _ in range(3)]

    def push(self,value):
        self.top += 1
        self.arr[self.top] = value
    
    def pop(self):
        value = self.arr[self.top]
        self.top -= 1
        return value
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop(), end='')
print(stack.pop(), end='')
print(stack.pop(), end='')

# 출력
# 3 2 1
print()
print('-'*20)
print('Queue객체')
from queue import Queue
def foo(n, x: list):
    q = Queue()
    q.put(n) # n을 Queue 에 삽입
    while not q.empty(): # queue가 비어있을리 없으므로, 방어코드
        m = q.get() # 가장 먼저 넣은 값 n이 m에 할당
        # print('m: ', m) # 테스트용 코드
        if m < len(x): # 만약 m이 주어진 리스트의 길이보다 작으면
            q.put(x[m]) # 리스트의 m번째 요소를 q에 추가한다.
        print(m, end='')
foo(3,[1,2,3,4,5])
print()

# x가 정수로 이루어진 리스트라면, IndexError는 발생하지 않을까?
# 발생한다.... 정수여도 음의 정수(배열의 길이를 벗어난)가 있다면 에러발생한다.

# 아래의 코드는 Queue객체를 이용하든, LifoQueue객체를 이용하든, 어차피 값을 1개만 삽입했다가, 바로 빼는 과정을 거치므로, 같은 결과를 갖는다.
print('LifoQueue객체')
from queue import LifoQueue
def foo1(n, x:list):
    q = LifoQueue()
    q.put(n)
    while not q.empty():
        m = q.get()
        # print('m: ', m) # 테스트용 코드
        if m < len(x):
            q.put(x[m])
        print(m, end='')
foo1(3,[1,2,3,4,5])