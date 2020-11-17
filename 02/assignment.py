# 치환문

# literal로 대입 (값이 되는 것을 literal이라고 함)
a = 1

# 변수 이름으로 대입
b = a

# 연산식
c = a + b

print(a, b)


# 여러 개를 한번에 치환
e, f, g = 3.5, 4.5, 9.8

# ,를 찍으면 같은 라인에 스페이스 되어 표시됨
# print(a, b)

# swap
x = 10
y = 20
print(x, y)
temp = x
x = y
y = temp
print(x, y)

# 파이썬 swap
x = 100
y = 200
print(x, y)
x, y = y, x
print(x, y)

a = 10
a += 10
print(a)

a -= 3
print(a)
a *= 2+3
print(a)
