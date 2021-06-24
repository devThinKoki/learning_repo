# print('-'*20)
# for i in range(3):
#     for j in range(1,4):
#         print("'" * j, end=' ')
#     print()

# print("""
# ' '' '''
# ' '' '''
# ' '' '''
# """)
# print('-'*20)
# word = input()

# # Change the next line
# print(word*2)
# print('-'*20)

# implement the function below
# def get_sum(a, b):
#     return a+b

# print('-'*20)

# import math

# radian = float(input())
# sinx = math.sin(radian)
# cosx = math.cos(radian)
# if sinx > cosx:
#     print(sinx - cosx)
# else:
#     print(cosx - sinx)


# print('-'*20)
# file = open('test_file.txt', 'w')
# file.write('This line will be in the file!')
# file.close()

# print('-'*20)
# x, y = float(input()), float(input())
# # print(x, y)
# # print(type(x), type(y))
# if x == 0 or y == 0:
#     if x == 0 and y == 0:
#         print("It's the origin!")
#     else:
#         print("One of the coordinates is equal to zero!")
# else:
#     if x > 0 and y > 0:
#         print('I')
#     elif x < 0 and y > 0:
#         print('II')
#     elif x < 0 and y < 0:
#         print('III')
#     else:
#         print('IV')
# print('-'*20)

# int_datas = []
# while True:
#     i = input()
#     try:
#         i = int(i)
#         int_datas.append(i)
#     except:
#         break
# sum = 0
# for num in int_datas:
#     sum += num
# print(sum / len(int_datas))
# print('-'*20)

    # there is a dictionary by default.
    # squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}
    # read the input as a key that needs to be deleted from the dictionary and print the value of this key.
    # if input key does not exist in dictionary. then you need to print("There is no such key")
    # Finally print the squares dictionary on the next line after all the changes.

# key = int(input())
# if key in squares.keys():
#     value = squares[key]
#     del squares[key]
#     print(value)
# else:
#     print("There is no such key")
# print(squares)