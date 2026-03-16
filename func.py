#사용자 정의 함수

#함수 : 특정한 작업을 수행하기 위해 필요한 명령어들을 묶어 놓은 것

#<함수 정의 - def (define)>
# def 함수명 (매개변수1,매개변수2,...,매개변수n)
#   실행명령
#   return 반환 값

def func1():
    pass #pass : 아무것도 하지 않고 넘어감.
#   문법상 코드가 있어야 하지만 아직 작성하지 않았을 때 쓰는 빈 명령어(placeholder)

#----------------------------
def rect_area(x,y):
    return x*y, (x+y)*2

#반환 값이 여러개면 튜플로 반환됨
print (rect_area(10,20))

#변수 개수를 맞춰서 반환값을 받으면 각 변수에 하나씩 반환됨.
area, length = rect_area(10,20)
print(area)
print(length)

#----------------------------
#(연습)정수를 입력하면 짝수인지 홀수인지 판별해주는 함수
def checkOddEven(x):
    if int(x)%2==0:
        result = "짝수"
    else :
        result = "홀수"
    return result

print(checkOddEven(2))
print(checkOddEven(7))

#----------------------------
#함수를 정의할 때, default 값을 지정할 수 있다.
def like_fruit(name, fruit="apple"):
    print(f"{name}님이 제일 좋아하는 과일은 {fruit}입니다.")

#함수를 호출할 때, 매개변수의 순서에 맞추어서 전달.
like_fruit("이순신") #매개변수1개만 전달, 나머지는 디폴트로 적용
like_fruit("이순신","orange")

#매개변수 명을 지정하면, 매개변수의 순서에 상관없이 호출 가능.
like_fruit(fruit="orange",name="이순신")
#----------------------------
def avg(*num): #매개변수를 여러 개 받을 수 있음
    count = len(num) #요소의 개수를 반환
    sum = 0
    for i in num:
        sum = sum+i
    return sum/count #총합/전체개수

print(avg(10,20,30,40,50))

#----------------------------
#지역변수, 전역변수

pi=3.1 #전역변수

def circle_area(r):
    # 파이썬은 함수 안에서 변수를 대입하면 기본적으로 지역변수로 취급됨.
    #pi += 0.04 # 실행 시 pi를 지역변수로 인식, 초기값이 없어 UnboundLocalError 오류 발생
    
    global pi # 전역변수를 바꾸려면 전역변수 선언(global)을 통해 함수 내부에서 전역 변수 사용
    pi += 0.04 # 선언 이후 함수 내부에서 count 값을 수정 가능
    a = r*r*pi
    return a

result = circle_area(10)
print(f"원의 넓이는 {result}입니다.")
#print(a) #not defined #a는 함수 내의 지역변수이므로 에러 발생.

#----------------------------
#lambda
#람다 : 보통 함수를 간결하게 만들 때 사용
#def를 사용할 수 없는 곳이나 혹은 매우 간결한 함수를 사용 시
#lambda 매개변수1, 매개변수2,..., 매개변수 : 표현식

def add(x,y):
    return x+y

add = lambda x, y : x+y #위와 동일.
print(add(10,5))

#lambda에서는 if 조건문을 삼항 연산자 형태로 사용 가능
#lambda 매개변수: (값1) if 조건 else (값2)

#조건식이 참이면 앞의 매개변수로 반환
is_even = lambda x : "짝수" if x%2 == 0 else "홀수"
print(is_even(2))

#중첩 조건 (괄호 사용)
grade = lambda x : "A" if x>=90 else ("B" if x>=80 else "C")
print(grade(95))
