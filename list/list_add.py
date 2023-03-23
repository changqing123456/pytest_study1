# 列表推导式
a = []
for i in range(1, 10):
    a.append(i)
print(a)
print([b**2 for b in range(1, 10) if b > 5])
print([c for c in range(1, 10)])
