numbers = list(map(int, input('Nhap:').split()))
s = set()
v = []
for num in numbers:
    if num not in s:
        v.append(num)
        s.add(num)
a = [0] * len(v)
s = 0
for x in v:
    for num in numbers:
        if num == x:
            a[s] += 1
    s += 1
pos = a.index(max(a))
print(v[pos])