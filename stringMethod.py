#String 클래스 문자열처리함수 실습

str = " abcabctd "
str = str.strip() #문자열 앞/뒤 공백 제거

print(str.count('a')) # 문자 개수 세기
print(str.index('d')) # 문자의 인덱스 반환(없으면 에러!!)
print(str.find('f')) # 문자의 인덱스 반환(없으면 -1반환)
print(str.replace('abc','o')) #abc를 o로 대체하기

data = " henry, 010-1234-5678  "
print(data.strip())
print(data.split(','))

