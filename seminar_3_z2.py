n = int(input('Введите количество элементов в массиве: '))
x = int(input("Введите число x: "))
A = list(range(1,n+1))
print("Элементы массива:")
print(A)

b=[abs(A[i]-x) for i in range(len(A))]
print(A[b.index(min(b))])