#함수는 객체다 -> 함수의 파라미터로 전달할 수 있다
#a = 10

#f(a)
#f(20)

#def f():
#    pass

#func(f)

#100 = f(10)

#f2(100)
#f2(f(10))



print ('=============== lambda ===============')
def blah(x):
    return x * 2

for i in range(10):
    print(f'{i}:{blah(i)}', end=' ')
else:
    print('')


# 다른 언어에서는 (x => x*2)(i)
for i in range(10):
    print(f'{i}:{(lambda x: 2*x)(i)}', end=' ')
else:
    print('')
