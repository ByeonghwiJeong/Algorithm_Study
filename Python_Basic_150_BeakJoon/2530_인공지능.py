A, B, C = map(int, input().split())
D = int(input())

E, s = divmod(D, 60)
h, m = divmod(E, 60)

A += h
B += m
C += s

if C >= 60:
    B += 1
    C -= 60
if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A %= 24
print(A, B, C)
