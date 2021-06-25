# Q3. 다음 중 copy 수행과 deepcopy 수행 결과가 같은 객체는?
# a = ('a','b', ['c','d'])
# b = {3: [1,5], 5: [10,20]}
# c = []
# d = (((((1) ,),),),)
# import copy
# a1 = copy.copy(a)
# a2 = copy.deepcopy(a)
# print(id(a),id(a1), id(a2))
# print(id(a1[2]), id(a1[2]), id(a2[2]))
# print(id(a1[2][0]), id(a1[2][0]), id(a2[2][0]))

# b1 = copy.copy(b)
# b2 = copy.deepcopy(b)
# print(id(b),id(b1), id(b2))
# print(id(b[3]),id(b1[3]), id(b2[3]))
# print(id(b[3][0]),id(b1[3][0]), id(b2[3][0]))

# c1 = copy.copy(c)
# c2 = copy.deepcopy(c)
# print(id(c),id(c1), id(c2))
# c.append(2)
# print(c,c1,c2)

# d1 = copy.copy(d)
# d2 = copy.deepcopy(d)
# print(id(d),id(d1), id(d2))
# print(id(d[0]),id(d1[0]), id(d2[0]))
# print(id(d[0][0]),id(d1[0][0]), id(d2[0][0]))
# print('답: d')



# Q8. 조건에 맞는 함수 완성]
# def prob8(x, y):
#     # 두 리스트 x, y에서 일치하는 자료의 수를 반환
#     # 시간 복잡도는 O(N)으로 하기.
#     # 이때, N = max(len(y), len(x))
#     result = set(x) & set(y)
#     return len(result)

# Q9. 조건에 맞는 함수 완성
def prob9(x):
    # 파이썬 내장 정렬 함수를 사용하지 않고, 정수가 담긴 리스트 x를 정렬하시오
    # x가 이미 정렬된 리스트라면, 시간복잡도가 O(N)이 되도록 하시오.
    # 공간 복잡도는 O(1)로 하시오.
    # 즉, 변수 하나만 가지고 사용하라는 뜻.

    smallest = 0
    changed = 0
    for idx in range(1, len(x)): 
        if x[idx] < x[smallest]:
            x[idx], x[smallest] = x[smallest], x[idx]
    smallest += 1
    print(x)

prob9([1,5,3,9,7,8])

#   Q10
# 재귀함수로 구현하기
# 정수 X가 정수 Y의 N제곱(N: 0이상의 정수)인지 여부를 반환
# def prob10(x, y):
#     if x // y == 0:
#         return 0
#     else:
#         return prob10(x//y, y ) + 1
# print(prob10(1000,10))