a = (1, 2, 3)
b = (1, 2, 3)
print(a+b)
print(tuple(a[x] + b[x] for x in range(len(a))))
a[0] = 4
print(a)