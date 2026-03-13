# 리스트
## 리스트 생성
data1 = []
data2 = [1,2,3]
data3 = ["henry","tom","max"]
data4 = ["henry",24,178.5,True] # 다양한 타입이 함께 들어갈 수 있다.
print(data3[2][2]) # x

##리스트에 요소 추가하기.append(추가할요소)
data4.append(False)
print(data4)

##리스트에 요소 끼워넣기.insert(위치,추가할요소)
data4.insert(0,"Student")
print(data4)

##리스트 수정
data3[0] = "HENRY"
print(data3)

##리스트 삭제
###리스트.remove(삭제할 요소)
###리스트.pop(인덱스)
###리스트.clear() - 비어있는 리스트로 만듬.
data4.remove(True)
print(data4)

data4.pop(2)
print(data4)

data4.clear()
print(data4)

## 리스트의 연산
data = data2+data3
print(data)
print(data*3)
