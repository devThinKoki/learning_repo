# class Stack:
#     def __init__(self):
#         # 여기에 코드 작성
#         self.top = -1
#         self.arr = [False for _ in range(3)]

#     def push(self,value):
#         self.top += 1
#         self.arr[self.top] = value
    
#     def pop(self):
#         value = self.arr[self.top]
#         self.top -= 1
#         return value
    
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop(), end='')
# print(stack.pop(), end='')
# print(stack.pop(), end='')

#출력
# 3 2 1


from queue import Queue
def foo(n, x: list):
    q = Queue()
    q.put(n) # n을 Queue 에 삽입
    while not q.empty(): # queue가 비어있을리 없으므로, 방어코드
        m = q.get() # 가장 먼저 넣은 값 n이 m에 할당
        print('m: ', m)
        if m < len(x): # 만약 m이 주어진 리스트의 길이보다 작으면
            q.put(x[m]) # 리스트의 m번째 요소를 q에 추가한다.
        print(m, end='')
foo(3,[1,2,3,4,5])
print()

# x가 정수로 이루어진 리스트라면, IndexError는 발생하지 않을까?

from queue import LifoQueue
def foo1(n, x:list):
    q = LifoQueue()
    q.put(n)
    while not q.empty():
        m = q.get()
        print('m: ',m)
        if m < len(x):
            q.put(x[m])
        print(m, end='')
foo1(3,[1,2,3,4,5])