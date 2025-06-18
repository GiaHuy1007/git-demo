numbers = list(map(int, input('Nhap:').split()))
v = []
s = set()
for num in numbers:
    if num not in s:
        v.append(num)
        s.add(num)
print(v)