# 객체 카피



print("============= reference copy =============")
#a = 1
#b = a
#a = [1, 2, 3]
import copy

a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)


print("============= swallow copy (얕은 복사) =============")
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.copy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]

a = b[:]






print("============= deep copy (깊은 복사) =============")
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.deepcopy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])


print("====== 복합객체(container)가 한개만 있는 경우 깊은/얕은 copy는 별 차이가 없다 ======")
a = ["hello", "world"]

b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

c = copy.deepcopy(a)
print(a is c)
print(a[0] is c[0])




