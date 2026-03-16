#mod_name 모듈의 info()를 테스트하려면 mod_name을 임포트해야 함.

#[방법1] 모듈명으로 임포트, 함수 사용 시 .으로 모듈 접근 필요
#import mod_name
#mod_name.info()

#[방법2]
# 모듈 내 함수명으로 임포트하면 mod_name.info() 대신 info()로 바로 사용가능하다.
from mod_name import info
info()




