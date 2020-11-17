# 복소수 실수부+허수부
# 허수부는 수학에서는 i로 표시했지만, 파이썬에서는 j, J를 숫자뒤에 붙인다.

a = 4 + 3j
print(a, type(a))

# 복소수 연산
b = 7 - 2j
print(a + b)
# complex 함수를 이용하여 복소수 타입의 객체를 만들 수 있다.
print(b.real, b.imag)


a = 6
print(0 < a < 10)
print(0 < a and a < 10)
print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] > [1, 2, 0])
