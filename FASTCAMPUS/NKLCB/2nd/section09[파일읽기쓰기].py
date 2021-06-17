# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\review.txt', 'r')
contents = f.read()
print(contents)
print(dir(f))
# 반드시 close()를 호출하여 open한 파일을 닫아주어 리소스 반환해야 한다.
f.close()

print()

# 예제2
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\review.txt', 'r') as f:
    c = f.read()
    print(iter(c)) # for문을 사용할 수 있도록 iter객체 반환
    print(list(c)) # 각 문자단위로 list에 담아 반환
    print(c)

print()

# # read : 전체 내용 읽기, read(10) : 10글자 읽기

# # 예제3
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\review.txt', 'r') as f:
    for c in f: # f자체가 iterable하므로 for문 사용 가능
        # print(c)
        print(c.strip())

print()

# # 예제4
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)  # 내용 없음
    # 위에서 read()로 이미 내용을 다 읽었으므로, 내용이 없다.
    f.seek(0, 0)  # 커서를 다시 내용의 처음 부분으로 옮김
    contents = f.read()
    print('>', contents)
print()

# # readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

# # 예제5
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
print()

# # readlines : 전체 읽은 후 라인 단위 리스트 저장
# # 예제6
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end=' ')
print()

# # 예제7
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))

# # 파일 쓰기

# # 예제1 (해당이름의 파일이 없으면 새로운 파일을 생성)
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\test.txt', 'w') as f:
    f.write('niceman!1')

# # 예제2 (해당이름의 파일이 없으면 새로운 파일을 생성, 있으면 기존 파일 맨 끝에 붙여씀)
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\test.txt', 'a') as f:
    f.write(' niceman!!2')

# # 예제3
from random import randint

with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\score1.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 47)))
        f.write('\n')

# # 예제4
# writelines : 리스트 -> 파일로 저장
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# # 예제5
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec09_resource\test3.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)
