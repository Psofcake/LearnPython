class Animal:
    def __init__(self,n):
        self.name=n

    def speak(self):
        return "소리를 냅니다"
    
class Dog(Animal): #Animal 상속
    def speak(self): #메서드 오버라이딩 (다형성)
        return f"{self.name}가 멍멍 소리를 냅니다"
    
class Cat(Animal): #Animal 상속
    def __init__(self,n,c):
        super().__init__(n) #부모 생성자 호출
        self.color = c
    def speak(self): #메서드 오버라이딩 (다형성)
        return f"{self.color} {self.name}가 야옹 소리를 냅니다"

dog=Dog("초코")
print(dog.speak())

cat = Cat("나비", "검정색")
print(cat.speak())

# 참고 - 파이썬은 다중 상속도 지원합니다. (예:class SmartPhone(Phone, Camera): - Phone, Camera 상속)
