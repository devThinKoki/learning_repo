# Section11
# 파이썬 예외처리의 이해
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec11_[csv]_resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵: 가장 상위 컬럼(행)을 읽는 것을 스킵함
    # 확인 
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__가 있는 것을 확인 => for문 사용가능
    print()

    for c in reader:
        print(c)

# 예제2
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec11_[csv]_resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자로 '|'을 선택
    # next(reader) Header 스킵: 가장 상위 컬럼(행)을 읽는 것을 스킵함
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__가 있는 것을 확인 => for문 사용가능
    print()

    for c in reader:
        print(c)

# 예제3 (Dict 변환)
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec11_[csv]_resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-----')

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec11_[csv]_resource/sample3.csv', 'w', newline='') as f:  # newline='' 테스트
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    print(type(wt))
    for v in w:
        wt.writerow(v) # 한 줄 한 줄 검사하고 써야 할 경우

# 예제5
with open(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec11_[csv]_resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    print(type(wt))

    wt.writerows(w) # 이미 검수가 끝난 데이터들을 파일을 쓸 경우,


# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install pandas 설치 필요
# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함
# pandas: 데이터 과학, 분석을 하기 위한 이전 단계에서 열과 행의 데이터 셋, 프레임 셋을 만들어서
#       정확한 통계를 추출하기 위한 셋을 만들어줌
#       numpy 등이 함께 설치됨.(openpyxl, xlrd 등을 내부적으로 사용함) 
 
  
print('-'*20,'import pandas','-'*20)
import pandas as pd
# sheetname='시트명' 또는 숫자, header=숫자, skiprow=숫자 등의 attribute를 갖는다.
# sheetname='시트명' 또는 숫자, header=3, skiprow=1 실습
import os
xlsx = pd.read_excel('./2nd/sec11_[csv]_resource/sample.xlsx')
# 상위 데이터 확인
print(xlsx.head())# head(): 위에서 5개(default값)row만을 출력
print()

# 데이터 확인
print(xlsx.tail()) # tail(): 아래에서 5개(default값)row만을 출력
print()

# 데이터 구조
print(xlsx.shape) # shape(): 행, 열의 개수를 튜플로 반환


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./2nd/sec11_[csv]_resource/result.xlsx', index=False)
xlsx.to_csv(r'D:\LocalServer\learning_repo\FASTCAMPUS\NKLCB\2nd\sec11_[csv]_resource/result.csv', index=False)