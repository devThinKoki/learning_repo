# 계좌 관리 class 작성하기
#   -attribute: 계좌 초기 금액을 속성으로 설정
#       -생성자에서 초기 금액은 0으로 설정
#       - 속성은 private으로 설정
#   -method: 인출, 저축, 잔액 확인 세 가지 method구현,
#       - 각각 현재 계좌 금액 리턴
#       - 각 method도 private으로 설정

class account_mgmt:
    def __init__(self, amount = 0):
        self.__amount = amount
    
    def __withdraw(self, amount):
        if amount > self.__amount:
            print('Not enough amount of money on your account')
            return
        self.__amount -= amount
        print('Current amount: ', self.__amount)
        return self.__amount

    def __saving(self, amount):
        self.__amount += amount
        print('Current amount: ', self.__amount)
        return self.__amount

    def __getCurAmount(self):
        print('Current amount: ', self.__amount)
        return self.__amount

# ac = account_mgmt(0)
# for d in dir(ac):
#     print(d)
# ac._account_mgmt__saving(10000)
# ac._account_mgmt__withdraw(1000)
# ac._account_mgmt__getCurAmount()


# 학생 성적 관리 class 작성하기
#   -attribute:
#       - 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정
#       - 각 속성은 private으로 설정
#   -method: 전체 과목 점수 평균, 전체 과목 총점 두 가지 method 구현
#       - 각 method는 private으로 설정

# 피자 가게 관리 class 작성하기
#   -attribute: 피자 종류(리스트 형), 피자 가게 이름
#       - 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정
#       - 피자 종류는 ['슈퍼스프림', '콤비네이션', '불고기']로 제공
#   -method: 원하는 피자를 제공하는지를 알려주는 기능
#       - Yes 또는 No 문자열을 리턴