a=1
b=2

if a==1 and b==2:
    print(a+b) #들여쓰기 필수. 안쓰면 에러남.

if a==0:
    print(a)
elif b==a: #elif = else if
    print(b)
else:
    print("해당없음")

# PRACTICE 1
# 주민번호에서 성별을 분석하여 '남성','여성'으로 출력하기
id1 = "990101-1******"
id2 = "990202-2******"
id3 = "260303-3******"
id4 = "260404-4******"

id = id1
sNumber=id.split('-')[1][0]

print(sNumber)
if sNumber=='1' or sNumber=='3':
    print("남성")
else:
    print("여성")

# PRACTICE 2
# 오늘 날짜가 홀수면 "홀수번호 차량 통행가능"
# 오늘 날짜가 짝수면 "짝수번호 차량 통행가능" 출력

date = "2026-03-13"
if int(date.split('-')[-1])%2==0:
    print("짝수번호 차량 통행가능")
else:
    print("홀수번호 차량 통행가능")

# PRACTICE 3
# 구매금액+배송비(3000원) 총 결제 금액을 출력.
# 50000원 이상은 무료배송.

price = 25000

if price<50000:
    price=price+3000
print(f"결제금액은 {price}원 입니다.")
