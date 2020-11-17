# if ~ elif (그렇지 않고 ~이면) ~ else   if는 있어야 되고 else는 옵션
# if ~ else : ~이거나 아니거나
a = 2

if a > 5:
    print('big')
#elif a <= 5:
#    print('small')
else:
    print('small')

# if ~ elif ~ else

b = 0
if b > 0:
    print('양수')
elif b < 0:
    print('음수')
else:
    print('0')

order = 'milk'
price = 0
# spam price: 1000
# milk price: 500
# egg price: 100
if order == 'spam':
    price = 1000
elif order == 'milk':
    price = 500
elif order == 'egg':
    price = 100
else:
    price = '없는상품'


print(f'가격:{price}')



