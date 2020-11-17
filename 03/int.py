# 정수형 연산자

a = 23
b = 20 + 3

print(a, type(a))
print(b, isinstance(b, int))
print(b, isinstance(b, bool))
# instance는 지정값이 정수이냐, 지정값이 boolean이냐를 object 개념으로 처리됨

# 2진수, 10진수, 8진수, 16진수

# c = 1101
# 이렇게 하면 파이썬이 10진수로 인식하기 때문에 2진수라는 것을 알려주어야 한다.
c = 0b1101
print(c)

d = 0o23
print(d)

e = 0x23
print(d)

# python 3.x에서 long형이 없어지고 int 타입으로 처리됨.(합쳐졌다) 따라서 표현범위가 무한대다.
e = 2**1024
print(e, type(e))
print(e.bit_length())
# .은 객체

# 변환함수
print(oct(38))
print(hex(38))
print(bin(38))
