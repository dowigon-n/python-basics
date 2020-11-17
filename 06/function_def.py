# y = f(x)
# f(x) = ax+b
# 이게 신경망이다.

# def f(x):          #x를 parameter, argument function (편각함수)
# 반복되는 작업들은 함수로 작성

# 함수정의

#java로는 함수를 {}로 범위를 막아놓을 수 있음
#function dummy(){

#}

print ('=============== 함수정의 ===============')
def dummy():              #아무것도 안하는 함수
    pass
#입력도 없고 반환값이(return) 없는

def func1():
    print('Hello World')
#입력은 있는데 반환값이 없는

def func2(name):
    print('Hello' + name)

# parameter 없이 다 가져오게 하는
def func3():
    return 'Hello World'

def times(a, b):
    return a * b

dummy()
func1()
func2('서범진')
s = func3()                     #반환값을 받고 출력하면 됨
n = times(2, 2)                 #빈환값을 받고 출력하면 됨
print(s, n)

print ('파이썬은 객체 하나만 반환할 수 있다는 것을 기억할 것')

print ('=============== 여러 값을 반환할 수 있다 ===============')

def func4():
    return 10, 20   # tuple auto packing을 통해 tuple 객체 하나를 반환한다.
t = func4()
print(t, type(t))

a, b = func4()      # tuple auto unpacking을 통해 반환된 tuple 객체를 여러 변수에 대입할 수 있다.
print(a, b)


print ('=============== 함수도 객체다. ===============')
#한국은 SI에 편중되어 java 비중이 큼
# framework가 특정 언어 기반 아니면 같이 일 못한다는 등 java 비중이 그만큼 크다는 말.

#가변 파라미터, 디폴트 파라미터 를 가지는 함수를 어떻게 할지 아규먼트 다양한 파라미터와 함수 중요
print(func1)
print(id(func1))
print(type(func1))


f = func1()
f()

# import : 다른 걸 끌어다 쓰는 것

# data = "........."
#
# r = ......
#
# f1(s):
#    r = .........
#    return r
# f2(s):
#    r = .........
#    return r
# f3(s):
#    r = .........
#    return r
#       s1 = f1(data)
#       s2 = f(s1)
#       result = f3(s2)

#       filters = [f2]                    2) 이렇게도 가능하다 유연하다 flexible
#       result = f3(f2, f1, data)         1) 파이썬에서는 f3를 호출하면서 줄줄이 가능하다
#       result = f3([f2, f1], data)       3) 이렇게 파라미터를 넘기면서 일목묘연하게 데이터의 흐름을 볼 수 있다.
# 객체를 함수로 가지는 점이 유용하다는 점
# 프로그래밍 트렌드 상에서 함수를 객체로 사용하고 데이터 흐름을 쭉 연결하는... 함수형 프로그래밍이라 함..
# 파이썬은 다 객체다

#def f1(s):
#    return s.upper()
#
#def f2(s):
#    return s[-1::-1]
#
#def f3(s):
#    return s+'!'
#
#print(f3(f2(f1('data'))))
#print(f3([f2, f1], 'data'))



