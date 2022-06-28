'''
1. 캠핑장은 연속하는 20일중 10일동안만 사용가능
2. 강산이는 28일의 휴가를 이제막 시작함
연속하는 P일중,
L일동안만 사용할 수 있다.
강산이는 이제 막 V일짜리 휴가를 시작
(1<L<P<V)
강산이는 캠핑장을 최대 몇일 동안 사용할 수 있을까?

입력)
    여러 개의 테스트 케이스로 이루어져 있다. 
    각 테스트는 한줄로 이루어져 있고,
    L, P, V를 순서대로 포함하고 있다.
    모든 입력정수는 int범위이다.
    마지막 줄에는  0 0 0(0 3개)가 주어진다.

[[  ]]
'''
import sys
input = sys.stdin.readline
cnt = 1
while True:
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V ==0:
        break
    chk = []
    while len(chk) < V:
        for _ in range(L):
            chk.append(1)
        for _ in range(P-L):
            chk.append(0)
    chk = chk[:V]
    print(f"Case {cnt}: {sum(chk)}")
    cnt += 1