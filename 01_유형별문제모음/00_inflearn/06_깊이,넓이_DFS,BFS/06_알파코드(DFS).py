'''
철수와 영희는 서로 편지를 암호화해서 주고 받는다.
영희 - 알파벳A > 1, 알파벳B > 2, ...., 알파벳Z > 26
철수 - "BEAN" 암호화시 25114 
    >>> 복호화시 >> BEAAD, YAAD, YAN, YKD, BEKD, BEAN
영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 얼마나 많은 방법이 있는지 구하세요.
입력)
 - 암호화된 코드 (0으로 시작 x, 최대길이 50)
25114
출력)
 - 몇가지의 방법이 있는지 각 경우를 출력(사전순으로)
 - 경우의 수 출력
BEAAD
BEAN
BEKD
YAAD
YAN
YKD
6
'''
def dfs(L, P): # L : res에 넣어준 숫자 길이, P : res에 넣어준 숫자 갯수
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            # print(res[j], end='')
            print(chr(res[j]+64), end='') # ord('A') = 65 \ ord('a') = 97
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                dfs(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L + 1] == i%10:
                res[P] = i
                dfs(L+2, P+1)

code = list(map(int, input()))
n = len(code) # 종착점
code.append(-1) # 마지막자리확인시 IndexError 방지
res = [] * (n + 3)
cnt = 0
dfs(0, 0)
print(cnt)
