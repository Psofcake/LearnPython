#input() : 사용자에게 입력을 받는다.
num1 = input("첫 번째 숫자를 입력하세요 : ") #입력 안내
print(num1)
num2 = input("두 번째 숫자를 입력하세요 : ")
print(num2)

print(f"{num1}+{num2}={num1+num2}") #str문자열 자료형
int(1.1) #실수를 int정수형 자료형으로 타입캐스팅(형변환)
int("12")  #문자를 int로 형변환

num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
print(f"{num1}+{num2}={num1+num2}")

print(bool("")) #빈 문자 x Flase값
print(bool(" ")) # True
