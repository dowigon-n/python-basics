print('================ 생성 ================')

l1 = []
l2 = [1, True, 'python', 3.14]
#l1[2] = 10 일때, 'python'과 기존 연결이 끊어지며 사라지고 객체 10이랑 연결됨
#이렇게 사라지는 데이터를 Gabage라 하고 파이썬에서 Gabage Collection이 존재


print('================ 인덱싱 ================')
print(l2[0])    # 가변 파라미터라고 함
print(l2[0], l2[1], l2[2], l2[3]) #처럼 여러개 paramether 입력가능
print(l2[-4], l2[-3], l2[-2],l2[-1] )
def f(x, y):
    return x + y


print('================ 반복 ================')
# 반복 (시퀀스 형태니까 반복 가능)
l3 = l2 * 2
print(l3)


print('================ 연결 ================')
l4 = l2 + [1, 2, 3]
print(l4)


print('================ 길이 ================')
print(len(l4))


print('================ in, not in ================')
print(5 in l4)
print(5 not in l4)


print('================ Slicing ================')
l5 = [0, 1, 2, 3, 4, 5]
print(l5[1:4])  #l5[1:4::1]  :1가 생략되어 있음
print(l5[0:6])
print(l5[:])
print(l5[2:])
print(l5[5::-1])   # :-1 은 역순
print(l5[-1::-1])


print('================ 변경가능한 객체(mutable) ================')
# 지우고자 할 때
del l5[2]
print(l5)
l5[1] = l5[1] + 1
print(l5)


print('================ 치환: slicing ================')
a = [1, 12, 123, 1234]
#a[0:2] = [10, 20]
a[0:2] = [100]
print(a)

a[1:2] = [200]
print(a)

a[2:3] = [300, 400, 500]
print(a)


print('================ 삭졔: slicing ================')
a = [1, 12, 123, 1234]
a[1:2] = []
print(a)

a[0:] = []   #슬라이싱을 많이 쓴다
print(a)


print('================ 삽입: slicing ================')
a = [1, 12, 123, 1234]

# 중간삽입
a[1:1] = ['a']
print(a)

# 마지막 삽입
a[5:] = [12345]   # a[5:5] = a[5:] 같음
print(a)

# 처음 삽입
a[:0] = [0]
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)


print('================ 객체함수: 삽입 ================')
a = [1, 3, 4]

# 중간에
a.insert(1, 2)
#a.insert(1, ['a', 'b', 'c'])
print(a)
# [1,   , 3, 4] 가 있다고 한다면
#      ↘
#    ['a', 'b', 'c'] 있는 그대로 삽입이 된 것임 (객체 하나가 추가된 것)

# 뒤에
a.append(5)
print(a)

# 앞에
a.insert(0, 0)
print(a)


print('================ 객체함수: reverse ================')
a.reverse()
print(a)


print('================ 객체함수: 삭제 ================')
#값으로 삭제
a.remove(3)
print(a)

try:
    a.remove(3)
except ValueError as e:
    print('값이 없는 경우 삭제시 예외 발생')


print('================ 객체함수: 스택으로 사용하기 ================')
# 스택 : 어떤 list가 있다고 할 때 특정 객체를 가져오거나 넣거나 삭제하는 게 정해져 있다 (동작 방식이 push 밖에 없음)
stck = []
stck.append(10)  #push
stck.append(20)  #push
stck.append(30)  #push
print(stck)

print(stck.pop())  #pop
print(stck.pop())  #pop

print(stck)

print('================ 객체함수: 큐(qeue) ================')
# 큐는 대량 데이터 처리 시 사용
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print(q)
