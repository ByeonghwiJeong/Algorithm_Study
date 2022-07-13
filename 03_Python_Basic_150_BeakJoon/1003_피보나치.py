'''
1 출력횟수 f(n)
0 출력횟수 f(n-1)
'''

chk = [(1, 0), (0, 1)]
for i in range(40):
    a1, b1 = chk[-2]
    a2, b2 = chk[-1]
    chk.append((a1+a2, b1+b2))
    
for _ in range(int(input())):
    N = int(input())
    print(*chk[N])

print(chk)
