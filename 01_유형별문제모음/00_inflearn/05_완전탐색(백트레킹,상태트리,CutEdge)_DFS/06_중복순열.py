'''
번호 1 ~ N 
중복허용하여 M번뽑아 출력
입력)
3 2
'''
N, M = map(int, input().split())
result = []
count = 0

def dfs(x):
    global count
    global result
    if x == M:
        count += 1
        print(*result, sep=' ')
        return
    for i in range(1, N+1):
        result.append(i)
        dfs(x+1)
        result.pop()

dfs(0)
print(count)
'''
구현방법 2가지
1) 넣고 빼기
result = []
result.append(i) & result.pop()
2) 오버라이딩해서 pop을 할필요없음
result = [0] * (N + 1)
result[x] = i
'''