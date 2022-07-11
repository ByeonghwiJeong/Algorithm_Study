N, M = 3, 3
a = [["*"] * N for _ in range(M)]
b = [[" "] * 9 for _ in range(9)]

b[0][:3] = a[0][:3]
print(*b, sep='\n')