#튜플
##튜플 생성
t1 = () #비어있는 튜플

t2 = (1,2,3)
t3 = 1,2,3
t4 = (1,) #데이터가 1개있는 튜플
t5 = ("henry",20,False) #다양한 타입 가능

#t5[0] = "Happy" #튜플 요소로 새로운 값을 대입할 수 없다.
print(t5[0])

# 튜플은 재할당(추가,변경,삭제)을 못하게 되어있다.
# 주로 반환 값을 받을 때 여러 개의 값을 리턴하면 튜플로 생성되어 반환된다.

fruit = ("apple","banana","orange")
a,b,c = fruit #a="apple",b="banana",c="orange"
print(a,b,c)
a,*b = fruit
print(a,b)
