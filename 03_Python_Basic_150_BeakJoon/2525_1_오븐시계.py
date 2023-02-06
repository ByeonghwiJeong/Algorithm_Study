A, B = map(int, input().split())
C = int(input())

h, m = divmod(C, 60)
A += h
B += m
if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24
print(A, B)