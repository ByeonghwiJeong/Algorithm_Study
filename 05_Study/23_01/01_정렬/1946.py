'''
다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 
적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다.

즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 & 면접 모두 떨어진다면 A는 선발 X
1 4
2 3
3 2
4 1
5 5 <<<
---
'''
import sys
input = sys.stdin.readline

def solve():
    global a
    a.sort()
    ans = 1
    tmp = a[0][1]
    for i in a[1:]:
        if i[1] < tmp:
            ans += 1
            tmp = i[1]
    return ans


for _ in range(int(input())):
    a = [tuple(map(int, input().split())) for _ in range(int(input()))]
    print(solve())
