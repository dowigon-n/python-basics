# while loop

print ('=============== while loop 기본 ===============')
#a = 0
#while a < 10:
#    print(a)
#    a = a + 1           # 이거 없으면 무한 loop 상태로 0 계속 출력

count = 1
while count < 11:
    print(count, end='')
    count += 1
else:
    print('')

# while문 보다는 for문 많이 선호 / 단, while문은 그 만의 장점이 있음
for a in range(10):
    print(a)

print ('=============== 1 ~ 10합 ===============')
s, n = 0, 1
while n <= 10:
    s += n
    n += 1
print(s)


print ('=============== break ===============')
i = 0
while i < 10:
    if i > 5:
        break
    print(i, end='')
    i += 1
else:
    print('---- end loop')


print ('\n============= continue ===============')
i = 0

while i < 10:
    i += 1      #이까지 닿지를 않음    그래서 i += 1을 if i<=5: 위에 올림 원래 print(i, end='') 아래 위치

    if i <= 5:              #이렇게 하면 무한루프에 빠져서
        continue            #여기서 계속 돌고
    print(i, end='')
else:
    print('---- end loop')

print ('============= infinite loop(무한루프) ===============')
i = 0
while True:
    if i > 5:
        break                     #i가 6되면 break 시키자 (빠져나오자)
        i += 1
else:
    print('else block')