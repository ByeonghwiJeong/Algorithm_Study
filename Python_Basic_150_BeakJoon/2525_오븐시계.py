A, B = map(int, input().split())
C = int(input())

h, m = divmod(C, 60)
add_h, ans_m = divmod(B+m, 60)
ans_h = (A + add_h + h) % 24
print(ans_h, ans_m)