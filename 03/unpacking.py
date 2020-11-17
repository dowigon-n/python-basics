# packing은 tuple로만 가능하다

t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking

a, b, c, d = t

print(a, b, c, d)  # 이게 언패킹임

# 오류: 패킹되어 있는 객체가 더 많은 경우
#a, b, c = t
# 오류: 패킹되어 있는 객체가 더 적은 경우
#a, b, c, d, e = t


# unpacking 확장
t = (1, 2, 3, 4, 5)
a, *b = t       # *가 있으면 tuple로 묶거나 풀 때 쓴다고 생각하면 됨

def f(*b):
    pass

f(1, 2, 3)


