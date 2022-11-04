'''
< 제로 >
https://www.acmicpc.net/problem/10773
문제)
- 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근수를 지우게하자
- 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어한다.
입력)
- 1     : 정수 K [1 \ 100,000]
출력)
- 
'''
import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    a = int(input())
    if a: l.append(a)
    else: l.pop()
print(sum(l))