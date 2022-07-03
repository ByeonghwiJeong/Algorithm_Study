max = float('-inf')
cnt = 0
for i in range(9):
    A = int(input())
    if A > max:
        max = A
        # print(i+1, max)
        cnt = i + 1
print(max)
print(cnt)