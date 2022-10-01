"""
https://www.acmicpc.net/problem/2661
숫자 1, 2, 3 으로만 이루어지는 수열이 있다.
임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면 <나쁜수열>
- 33
- 32121323
- 123123213
좋은 수열의 예
- 2
- 32
- 32123
- 1232123
길이가 N인 좋은 수열들을 
N자리의 정수로 보아 그중 가장 작은수를 
나타내는 수열을 구하는 프로그램 작성

길이5에서 특정 (1, 2, 3)중하나를 더할때 > 길이 6
[4:5] [5:6] 
[2:4] [4:6]
[0:3][3:6] 
7일경우에서 3가지 경우체크
"""
N = int(input())

def check(s, a):
    temp = s + a
    l = len(temp)
    for i in range(1, l // 2 + 1):
        if temp[l-i*2:l-i*1] == temp[l-i*1:l]:
            return False
    return True

def dfs(x, s):
    if x == N:
        print(s)
        exit()
    for i in range(1, 4):
        if check(s, str(i)):
            dfs(x + 1, s + str(i))

dfs(0, '')