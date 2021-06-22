a = [0, [1, [2, [3, [4, [5, None]]]]]]
b = [6, [7, [8, [9, [10, [11, None]]]]]]
c = a

# 해당 단원은 링크드 리스트인데... 왜 for문이 나왔지... 링크드 리스트처럼 풀려고 머리를 써보았는데..
# for문으로 해결할 수도 있긴 있구나..
# 이걸 어떻게 좀더 간단하게 구현할 수 있을까?

# 방법1: 다중for문
for i in range(1):
    c[i] = str(a[i]) + str(b[i])
    for j in range(1):
        c[i+1][j] = str(a[i+1][j]) + str(b[i+1][j])
        for k in range(1):
            c[i+1][j+1][k] = str(a[i+1][j+1][k]) + str(b[i+1][j+1][k])
            for l in range(1):
                c[i+1][j+1][k+1][l] = str(a[i+1][j+1][k+1][l]) + str(b[i+1][j+1][k+1][l])
                for m in range(1):
                    c[i+1][j+1][k+1][l+1][m] = str(a[i+1][j+1][k+1][l+1][m]) + str(b[i+1][j+1][k+1][l+1][m])
                    for n in range(1):
                        c[i+1][j+1][k+1][l+1][m+1][n] = str(a[i+1][j+1][k+1][l+1][m+1][n]) + str(b[i+1][j+1][k+1][l+1][m+1][n])
print(c)

# 방법2: for문
for i in range(1):
    c[i] = str(a[i]) + str(b[i])
    c[i+1][i] = str(a[i+1][i]) + str(b[i+1][i])
    c[i+1][i+1][i] = str(a[i+1][i+1][i]) + str(b[i+1][i+1][i])
    c[i+1][i+1][i+1][i] = str(a[i+1][i+1][i+1][i]) + str(b[i+1][i+1][i+1][i])
    c[i+1][i+1][i+1][i+1][i] = str(a[i+1][i+1][i+1][i+1][i]) + str(b[i+1][i+1][i+1][i+1][i])
    c[i+1][i+1][i+1][i+1][i+1][i] = str(a[i+1][i+1][i+1][i+1][i+1][i]) + str(b[i+1][i+1][i+1][i+1][i+1][i])
print(c)

print('-'*20)
while c:
    print(c[0], end='')
    c = c[1]

# 기대 출력
# 06172839410511