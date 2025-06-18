numbers = list(map(int, input('Nhap:').split()))
num, pos = map(int, input('Nhap ptu va vi tri can chen:').split())
numbers.insert(pos,num)
print(numbers)
