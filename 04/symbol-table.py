# global, local 심벌 테이블
# 노트 필기 참조

g_a = 1
g_s = '둘리'

def g_f():
    l_a = 2            #local
    l_s = '마이콜'      #local
    print(locals())


print("====== Global Symbol Table vs Local Symbol Table ======")
print(globals())
g_f()

print(g_a)
# 에러: local symbol table은 함수가 실행이 끝나면 사라지므로 l_a는 찾을 수 없다는 오류 발생
# print(l_a)

# 함수 안에도 객체가 있다
# 아래 1~6 그 객체에 대한 내용임
print("============ 01. 사용자 정의 함수 ============")
#심볼 테이블 있고, 확장 가능
g_f.n = 'Hello'
g_f.i = 10
print(g_f.__dict__)
# 개체가 확장이 가능하다는 의미

print("============ 02. 사용자 정의 클래스 ============")
# 심볼테이블 있고, 확장 가능
class MyClass:
    x = 10
    y = 10

MyClass.z = 30
print(MyClass.__dict__)

print("============ 03. 내장 함수 ============")
# 심볼테이블 x, 확장 x
# print.z = 10                # 확장이 안된다는 얘기는 symbol 이 없다는 의미
# print(print.__dict__)


print("============ 03. 내장 클래스 ============")
# 내장은 심볼테이블 있지만, 확장이 안된다.
# str.z = 10
print(str.__dict__)


print("============ 05. 사용자 정의 클래스로 생성된 객체 ============")
# 심볼테이블 있고, 확장 가능
o = MyClass()
o.z = 10
print(o.__dict__)


print("============ 06. 내장 클래스로 생성된 객체 ============")
# 심볼테이블 없고, 확장 안된다
g_a.z = 10
print(g_a.__dict__)
