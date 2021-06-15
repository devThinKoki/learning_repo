# list 자료형에 +=를 사용하면 새로운 리스트를 반환하는가?
li1 = [1,2,3]
print(id(li1), li1)
li1 += [2]
print(id(li1), li1)

# 
tup1 = (1,)
# tup2 = (2) # 요소가 하나인 튜플 생성시에는 ,를 추가해주어야 한다.
print(type(tup1), tup1)
# print(type(tup2), tup2)

# 출력값을 얻기 위한 변수b 생성하기
a = [1, '2', 3, '4']
b = {1:'a','2':'b', 3:'c', '4':'d'}
c = '.'.join([b[x] for x in a])
print(c)
# a.b.c.d

# 리스트 안의 튜플이 요소로 있다면, 튜플의 요소 변경이 가능할까?
tuple_in_list = [1,2,(3,4)]
tuple_in_list += [[2,3]]
print(tuple_in_list)
tuple_in_list[3] = '5'
print(tuple_in_list)
# tuple_in_list[2][1] = '2' # 불가능하다.
# print(tuple_in_list)