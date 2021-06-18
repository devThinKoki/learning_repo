class A:
    def __init__(self, x):
        self.x = x
    
    def __eq__(self,other):
        return id(self.x) == id(other.x)

x = [1]
a = A(x)
b = A(a.x)
c = A(x[:]) # x를 복사한 값(얕은 복사에 해당 새로운 주소값을 가지는 x의 값을 가짐)
d = A(a.x[:])

print( a==b, b==c, c==d)
# 출력 값:
# True False False


import copy
a = (1, 2, ['a', 'b'])
b = copy.deepcopy(a)
c = a[:]
d = copy.copy(c)
print(id(a), id(b), id(c), id(d))
a[2][1] = 1