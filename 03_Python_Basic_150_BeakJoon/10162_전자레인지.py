A = 100
B = 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        B -= a
    elif a < b:
        A -= b
print(A)
print(B)