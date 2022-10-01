"""
< 크게 만들기 >
https://www.acmicpc.net/problem/2812

N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰수를 구하는 프로그램을 작성하시오.
"""
N, K = map(int, input().split())
nums = list(map(int, list(input().rstrip())))
stack = []
for n in nums:
    while stack and stack[-1] < n and K > 0:
        # 스택에 자료가있고 이전값보다 다음값이 크고 K > 0
        stack.pop()
        K -= 1
    stack.append(n)

if K > 0:
    print(*stack[:-K], sep="")
else:
    print(*stack, sep="")
    
"""
스택을 사용해야 시간초과 발생 X
"""