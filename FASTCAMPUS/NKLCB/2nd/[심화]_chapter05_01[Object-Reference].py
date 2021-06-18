# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

print('EX1-1 -')
print(dir())

# id vs __eq__ (==) 증명
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x # 복사(copy)

print('EX2-1 -', id(x), id(y))
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y)      # 같은 객체를 담고 있으므로, x를 통해 객체를 수정해 주면, y도 수정된 값을 갖는다.

print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z) # 같은 객체일까? -> 같은 객체는 아니다. : 다른 주소에 할당된 서로 다른 객체이다.
print('EX2-8 -', x is not z) 
print('EX2-9 -', x == z) # 하지만 두개의 객체가 갖는 값은? -> 같다
print('EX2-10 - ', x.__eq__(z))

# # 객체 생성 후 완전 불변 -> 
# 즉, id는 객체 주소(정체성)를 비교,
#     ==(__eq__) 는 값을 비교
# ==을 이용해 값을 비교하는 것보다, is 로 주소를 비교하는 것이 속도가 훨씬 빠르다.
# 가령, 각각의 변수에 100만개의 데이터가 있다면, id만을 비교하는 is가 100만개의 값을 일일히 비교하는 ==(__eq__)보다 빠르다.
print()
print()

# # 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2)) # 서로 같은 값을 가지는 튜플 객체를 만들었지만, 객체는 만들어지는 순간에 주소가 할당되므로, id는 다르다.
#  불변형이 아닌, 리스트로 한번 확인해보자,
list1 = [10, 15] 
list2 = [10, 15]
print('EX3-1-2-', id(list1), id(list2)) # 즉, 변하는 리스트여도 객체를 생성한 시점이 다르면 서로 다른 주소를 갖는다.
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy(깊은 복사, 얕은 복사)
# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1 # copy()
tl3 = list(tl1) # (얕은 복사) 이는, 값은 같으나 리스트생성자인 list()를 사용하여 새로운 list객체를 반환하므로, 다른 주소를 갖게 된다.

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)

print()
# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3) # tl1에 새로운 값을 추가 삭제해 주었는데, 같은 주소를 참조하는 tl2에는 반영되었으나, tl3는 영향받지 않았다. 

print()
print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2) # 튜플 재 할당(객체 새로 생성)
print('EX4-10 -', tl3)
print(id(tl1[2])) # 리스트 안에 있던 튜플이 += 연산자로 새로운 튜플 객체로 바뀌었으므로, 리스트 안의 튜플이 갖는 주소값은 다르게 된다.
# 즉, 리스트안에 튜플을 요소로 갖는 것은 성능상 좋지않다.
# 계속 주소가 재할당되기 때문이다.
print()
print()

# # Deep Copy와 copy차이 확인하기
# 장바구니 클래스 생성
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 -', id(basket1), id(basket2), id(basket3))
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products))
# copy를 이용하여 객체를 복사하면, 표면적인 객체만을 복사하고, 깊숙한 곳의 객체들은 참조하는 것이고,
# deepcopy를 이용하면, 깊숙한 곳에 있는 객체들까지 복사하여 아예 새로운 객체로 생성해주는 것이다.
print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)

print()
print()


# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    return x

x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y)
print()
# 일반형일때는 


# 불변형 가변형일때는 어떻게 될까?
a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b) # 가변형 a -> 원본 데이터 변경
# 가변형 데이터는 원본 데이터의 값이 변경된 것을 알 수 있음
# 즉, 가변형 데이터가 함수의 매개변수로 전달되면, 주소가 전달되므로, 원래 데이터를 참조하여 변경이 이뤄지게 된다.

c = (10, 100)
d = (5, 10)

print('EX6-2 -', mul(c, d), c, d) # 불변형 c -> 원본 데이터 변경 안됨
# 불변형 데이터는 새로운 객체를 생성하게 되므로, 원본 데이터가 변경되지 않는다.
# 즉, 원본이 변해도 상관없다면, list형으로 함수에 보내는 것이 효율성이 좋다.
# 불변형의 경우엔 매번 새로운 객체가 생성되므로 원본은 유지할 수 있다.


# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 X -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))