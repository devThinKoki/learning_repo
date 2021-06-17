print('Q1: ', '-'*10)
def 함수funcname():
    print('한국어로 시작 가능?')

함수funcname()

class Reader:
    def __init__(self,file):
        self.file = open(file, 'r')
        self.is_done = False
    
    def read_char(self):
        #####코드작성부
        c = self.file.read(1) # 한 문자를 읽는다.
        if not c: # 읽힌 문자가 없다면, 다 읽었다는 뜻이므로,
            self.is_done = True # is_done 인스턴스 변수를 True로 바꾸어 준다.(while 탈출을 위함)
        return c # 읽은 c를 반환
        ####코드 작성부
        
reader = Reader(r'FASTCAMPUS\NKLCB\2nd\quiz-test\3.txt')
while not reader.is_done:
    print(reader.read_char(), end='')