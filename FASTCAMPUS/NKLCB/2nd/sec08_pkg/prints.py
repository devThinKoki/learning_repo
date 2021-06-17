def prt1():
    print("I'm NiceBoy!")

def prt2():
    print("I'm Goodboy!")

# 단위 실행(독립적으로 파일 실행)
# 패키지를 외부에서 import하여 실행하기 전에
# 테스트 해보고 싶을때를 위한 코드( 해당 코드는 독립적으로 실행될 때(__name__이 __main__일때)만 실행된다.)
if __name__ == "__main__":
    print("This is", dir())
    prt1()
    prt2()