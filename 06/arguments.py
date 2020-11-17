print ('=============== 기본 인수값 (default parameter) ===============')

def incr(a, step):
    return a + step

# a = incr(10)  이러면 에러인데 step 값이 필요하다는 얘기 step=1 뭐 이런식으로 def ~ 문단에 넣어도 됨


a = incr(10, 1)
print(a)

a = incr(10, step=5)
print(a)

a = incr(10, 5)
print(a)

# 문법오류
#def decr(step=1, a):
#    return a - step


print ('=============== 키워드 인수값 (Keyword Parameter) ===============')
# parameter 이름이 있는 것 (이름 지정)

def area(width, height):
    return width * height

print(area(10, 20))
print(area(width=10, height=20))
print(area(height=20, width=10))   # 위치를 다르게 해서 써도 된다
print(area(10, height=20))
# print(area(30, width=10))          # width 자리에 값이 있고 width 다른 값이 있으면 오류
# print(area(height=20, 10))


print ('=============== 가변 인수값 (Keyword Parameter) ===============')
def func2(*arg):          # 가변인수는 * 하나 붙여서 tuple로
    print(arg)

func2(10, 20)
func2(10, 20, 30)
func2(10, 20, 30, 40)
#func2([10, 20])
#func2([10, 20, 30])
#func2([10, 20, 30, 40])

def func2(a, *arg):
    print(a, arg)

func2(10, 20)
func2(10, 20, 30)
func2(10, 20, 30, 40)

# 모든 인수를 sum
def sum2(*arg):
    s = 0
    for n in arg:
        s += n
    return s

print(sum2())
print(sum2(1, 2))
print(sum2(1, 2, 3, 4, 5))
