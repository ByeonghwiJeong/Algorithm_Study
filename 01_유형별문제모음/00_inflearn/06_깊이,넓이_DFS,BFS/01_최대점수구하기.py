'''
현수는 N개의 문제를 풀려고 합니다. 
각 문제는 점수와 걸리는 시간이 주어지게 됩니다. 
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다. 
(해당문제는 해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)

▣ 입력설명
첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
5 20
10 5
25 12
15 8
6 3
7 4
▣ 출력설명
첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.
41
'''
import sys
input = sys.stdin.readline

def dfs(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        dfs(L + 1, sum + pv[L], time + pt[L])
        dfs(L + 1, sum, time)

n, m = map(int, input().split())
pv = list()
pt = list()
for i in range(n):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)
res = -2147000000
dfs(0, 0, 0)
print(res)