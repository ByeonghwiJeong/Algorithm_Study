'''
< 부분 수열의 합 > 
https://www.acmicpc.net/problem/1182
문제)
- N개의 정수로 이루어진 수열이 있다.
- 크기가 양수인 부분수열 중에서 
    그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를
    구하는 프로그램을 작성하시오.
입력)
-   1 : 정수개수N~[1\20], 정수S~[-1,000,000 \ 1,000,000]
'''
n, s = map(int, input().split())
a = list(map(int, input().split()))
ret = 0

def recur(i, sum): # i 인덱스??? 몇번 호출했는지 표시용 /// sum은 지금까지 더한 결과
    global ret
    if i == n: # 처음에 실수한부분은 그냥 저는 처음데 return하는 부분을 그냥 카운팅안하고 타겟값과 일치하는경우에 return해줫어요
        if sum == s: ret += 1
        return 
    recur(i + 1, sum + a[i]) # 첫번째는 +1  하나는 더하고 하나는 그냥 안더하는
    recur(i + 1, sum)

recur(0, 0)
if s == 0: ret -= 1
print(ret)
