# 부울(boolean) 참이나 거짓을 나타내는 값으로 두 가지 밖에 없음.
# True, False 두 literal만 가진다.
# 연산은 True(1), False(0)으로만 됨.

b0 = True
b1 = False

a = 1
b = 2

c = a * b
print(c)

# b3는 boolean에 대한 결과가 출력됨 (연산은 True (1), False (0) 으로 처리됨)
b3 = a > b

print(b3, type(b3))

b4 = b3 * 10
print(b4)

print(True * False)
print(True or False)


# 일반적으로 True, False를 정해놓고 쓰진 않는다.
# if나 while의 어떤 조건으로 많이 쓴다.

# Student라는 Class를 만든 것, Class는 나중에 배움.
# s1 = student(4, '둘리')
# s2 = Student(2, '마이콜')


