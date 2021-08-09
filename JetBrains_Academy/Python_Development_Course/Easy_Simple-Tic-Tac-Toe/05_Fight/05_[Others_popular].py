# write your code here
t = list('_________')
print("""---------
|       |
|       |
|       |
---------""")
c = 0
while True:
    while True:
        x, y = input('Enter the coordinates:').split()
        if not x.isdigit() or not y.isdigit():
            print('You should enter numbers!')
            continue
        x, y = [int(x), int(y)]
        if x < 0 or x > 3 or y < 0 or y > 3:
            print('Coordinates should be from 1 to 3!')
            continue
        if t[(x-1)*3+y-1] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        c = 1 - c
        t = list(t)
        if c:
            t[(x-1)*3+y-1] = 'X'
        else:
            t[(x-1)*3+y-1] = 'O'
        break
    print("---------")
    for i in range(0, 7, 3):
        print("| ", end='')
        for j in range(i, i + 3):
            print(t[j], end=' ')
        print("|")
    print("---------")
    t = ''.join(t)
    o = t.count('O')
    x = t.count('X')
    # print([list[i: i + 7: 3] for i in range(0, 7, 3)])
    if ("XXX" in [t[i: i + 3] for i in range(0, 7, 3)] or
          "XXX" in [t[i: i + 7: 3] for i in range(0, 3)] or
          "XXX" in t[0: 9: 4] or
          "XXX" in t[2: 7: 2]):
        print("X wins")
        break
    elif ("OOO" in [t[i: i + 3] for i in range(0, 7, 3)] or
          "OOO" in [t[i: i + 7: 3] for i in range(0, 3)] or
          "OOO" in t[0: 9: 4] or
          "OOO" in t[2: 7: 2]):
        print("O wins")
        break
    elif o + x < 9:
        # print("Game not finished")
        continue
    else:
        print("Draw")
        break