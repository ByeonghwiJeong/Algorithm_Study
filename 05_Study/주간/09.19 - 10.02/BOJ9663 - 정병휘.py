'''
NQueen
https://www.acmicpc.net/problem/9663
'''
N = int(input())
rows = set()  #  rows check
pos_diagonal = set() # - \
neg_diagonal = set() # + /
result = 0

def dfs(x):
    global result
    if x == N:
        result += 1
        return
    for i in range(N):
        if i in rows or x - i in pos_diagonal or x + i in neg_diagonal:
            continue
        rows.add(i)
        pos_diagonal.add(x - i)
        neg_diagonal.add(x + i)
        dfs(x + 1)
        rows.remove(i)
        pos_diagonal.remove(x - i)
        neg_diagonal.remove(x + i) 
dfs(0)
print(result)

'''
대각선과 row조건을 체크할때 if not () in visited형태로 반복했으나
깔끔하게 보이기위해서 visited 를 or조건으로 반복후 continue처리했다.
'''