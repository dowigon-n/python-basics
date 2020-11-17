# 논리연산자 (not, or, and)

a = 30
b1 = a <= 30
# not
# not True -> False
# not False -> True
b2 = not b1

# or (논리합)
# False or False -> False
# True or False -> True
# False or True -> True
# True or True -> True
b3 = a <= 30 or a > 100

# and (논리곱)
# False and False -> False
# True and False -> False
# False and True -> False
# True and True -> True
# b4 = a <= 30 and a >= 100
# b4 = a >= 100 and a <= 30
b4 = (a <= 30) and (a >= 100)
# b4 = 100 <= a <= 30

# print(b1, b2, b3, b4)
print(True or 'logivcal')
print(False or 'logical')
print([] or 'logical')
print([10, 20] or 'logical')

print('operator' or 'logical')
print('' or 'logical')
print('' or 'logical')

n = None
print(None or 'logical')

s = 'Hello World'
# if s is not '':
#    print(s)
# 위처럼 if 로 작성해야할 코딩을 아래처럼 간단하게 할 수 있다고 함
s and print(s) # 빈 문자열이면 출력하지 말고, 문자열이 이면 출력하게 하고 싶을 때

s = ''
s and print(s)

print('---------')

# 조건이 되어 반복을 많이 해야할 때