# 레퍼런스 카운트

import sys    # sys = 모듈

x = object()   # object = 객체
print(type(x))
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))

# 레퍼런스 값
del x         # del을 쓰는 이유는 symbol table 에서 날려버리기 위해
print(sys.getrefcount(y))       # x가 날아가버렸기 때문에 y로
# x는 symbol table에서 사라진다
#print(x)





