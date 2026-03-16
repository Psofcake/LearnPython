#클래스 --(인스턴스화)--> 인스턴스(속성, 메서드)

#클래스 : 객체를 만들기 위한 설계도 또는 틀
#인스턴스 : 클래스를 통해 만들어진 객체.

#속성 property : 객체가 가지는 고유한 특성(멤버 변수)
#메서드 method : 객체가 가지는 행동(객체 내 함수)

class CellPhone :
    #model = "M1"
    #factory = "Samsung"

    #클래스 객체 초기화
    def __init__(self,m,f,s) :
        self.model = m
        self.factory = f
        self.__serial = s #이중밑줄로 시작하는 변수는 name mangling으로 충돌 방지 적용. 관례적으로 private처럼 사용

    #self는 메서드를 호출한 객체 자신
    #인스턴스 메서드는 반드시 첫번째 매개변수로 self를 받아야함.
    def call(self):
        print("전화를 겁니다")
    def receive(self):
        print("전화를 받습니다")
    def send_msg(self):
        print("문자를 보냅니다")
    def info(self):     #키워드 self를 이용해서 멤버변수에 접근
        print(f"모델은 {self.model}이고, {self.factory}에서 만들었습니다.")
        print(f"시리얼 번호는 {self.__serial}입니다.")

p1 = CellPhone("m2","apple","1000") #생성자 실행
p2 = CellPhone("m3","samsung","9999")
p2.__serial = "8888" #기존 __serial을 수정하는 것이 아닌, 새로운 속성__serial을 추가하게 됨

p1.info()
p2.info()

#객체 지향의 특징
#캡슐화 : 멤버 변수를 클래스 안에서만 또는 클래스의 메서드를 통해서만 접근하고, 외부로부터 보호.
#상속 : 여러 클래스의 공통된 속성을 부모 클래스에 정의하고, 하위 클래스에서는 그에 맞는 특화된 속성과 메서드를 정의
#다형성 : 같은 이름의 메서드가 클래스 또는 객체에 따라 다르게 구현됨. 부모로부터 받은 동일한 이름의 메서드에 대해 각각 다른 동작을 수행하는 것.

