#for 반복문

## <형식>
## for 변수명 in 범위 : 범위-range,문자열,리스트 등
##  (들여쓰기 중요) 실행명령

## for 변수명 in range() :
##  (들여쓰기 중요) 실행명령

#range(시작,끝,스텝) : 시작(기본값 0)과 스텝(기본값 1)은 생략가능
# 끝 값은 필수. 시작값부터 끝값 미만까지 일정 간격(스텝)으로 반복

for i in range(0,3,1): # == for i in range(3)
    print(i) #0,1,2

sum = 0
for i in range(1,11) : #1~10까지 합 구하기, 스텝 생략
    sum+=i
print(f"1부터 10까지의 합은 {sum}입니다.")

for i in "apple":
    print(i) # a, p, p, l, e 출력

for i in ['a',1,False]: 
    print(i) # a, 1, False 출력
