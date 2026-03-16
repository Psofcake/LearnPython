#while 반복문

# <형식>
# 초기식
# while 조건식 : 
#   반복할 명령들
#   변화식

# break : 반복문 탈출
# continue : 코드 실행 건너 뛰기

i=1
sum = 0
while i<11:
    sum=sum+i #반복할 문장
    i=i+1 #변화식
print(f"1부터 10까지의 합은 {sum}입니다.")

#break
sum = 0
i = 1
while True:
    sum=sum+i
    i+=1
    if i>10:
        break
print(sum)

#continue
#(실습)1~10중 홀수만 출력하기
for i in range(1,11,2):
    print(i)

i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)

i=1
while i<11:
    print(i)
    i+=2
