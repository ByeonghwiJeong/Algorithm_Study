'''
< 가장 긴 증가하는 부분 수열 - O(NlogN)>
https://www.acmicpc.net/problem/12015
문제)
-  A = {10, 20, 10, 30, 20, 50}
- 부분수열 = {10, 20, 30, 50}
입력)
- 1     : 수열의 크기
- 2     : 

출력)
- 
'''
import sys
import bisect 
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
stack = [0]
for i in a:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect.bisect_left(stack, i)] = i
print(len(stack)-1)

'''
A = {10, 20, 10, 30, 20, 50, 25, 26 27}

stack = [0]

10 - 0 10
20 - 0 10 20
10 -   10
30 - 0 10 20 30
20 -         20
50 - 0 10 20 30 50
25 -            25
26 -	           26
27 - 0 10 20 25 26 27
'''