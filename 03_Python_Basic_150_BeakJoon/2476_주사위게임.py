v_max = float('-inf')
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    reword = 0
    if A == B and B == C:
        reword = 10000 + 1000 * A
    elif A == B or A == C:
        reword = 1000 + 100 * A
    elif B == C:
        reword = 1000 + 100 * B
    else:
        reword = max(A, B, C) * 100
    if reword > v_max:
        v_max = reword
print(v_max)
