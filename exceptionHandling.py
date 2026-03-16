#예외 처리(try ~ except)
# 프로그램이 에러로 중단되지 않고 안전하게 실행되도록 함

#try:
#   실행할 코드
#except Exception as e:
#   모든 예외 처리 (e에는 에러 메시지가 담김)
#else :
#   예외가 발생하지 않았을 때 실행 (에러 발생 시 실행되지 않음.)
#finally:
#   예외 발생 여부와 상관없이 항상 실행

try:
    a=int(input("인원입력:")) #a="1"입력 시 타입 에러 발생
    b=int(input("금액입력:"))
    c = b/a
except ValueError: #except는 위에서부터 순서대로 검사하고, 처음 매칭되는 except 실행 이후 나머지 except들은 체크되지 않음.
    print("숫자를 입력하세요")
except ZeroDivisionError: #나누는 수가 0일 때 제로디비전 에러 발생
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"에러:{e}")
else : print(f"한 사람당 {c}원씩 나누면 됩니다.") #에러가 발생하지 않으면 else 실행
finally:
    print("완료")

#----------------------------
#파일오픈
try:
    f = open("basic/output.txt","r") #경로가 없으면 현재 경로(swtest)에서 탐색. "r" == 읽기 위해 액세스함을 알림
except Exception as e:
    print(f"에러:{e}")
else: #문제없이 열리면 이하 실행
    print("파일열기 성공")
    f.close()

#----------------------------
#사용자 정의 예외 : 사용자가 의도적으로 예외를 발생시켜야 하는 경우
#raise 명령어 - 예외를 강제적으로 발생시킴.
def set_age(age):
    if age<0:
        raise ValueError("나이는 0 이상이어야 합니다.")
    return f"당신의 나이는 {age}살 입니다." # ==문자열 리턴

print(set_age(3))

