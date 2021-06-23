# list comprehension
list1 = [num for num in range(1,101)]
print(list1)

list2 = [num for num in list1 if (num % 3) ==0]
print(list2)

list3 = [num for num in list1 if not((num%3)==0 or (num%7)==0)]
print(list3)

# set comprehension
int_data = [1,1,2,3,3,4]
square_data_set = {num*num for num in int_data}
print(square_data_set)

# dict comprehension
id_name = {1: 'Dave', 2: 'David', 3: 'Anthony'}
print(id_name.items())
#아이디가 2 이상인 데이터를 이름: 아이디 형식으로 새로운 dict 만들기
name_id_dict = {key:value for key,value in id_name.items() if key >= 2}
print(name_id_dict)
# 아이디를 기존의 10배로 한번에 바꾸기
name_id_mul10 = {key*10:val for key,val in id_name.items()}
print(name_id_mul10)