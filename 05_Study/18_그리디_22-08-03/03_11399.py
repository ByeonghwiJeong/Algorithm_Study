'''
인하은행에는 ATM기 1대
N명의 사람이 줄을 서있다.

시간의 합의 최솟값
'''
N = int(input())
_times = list(map(int, input().split()))
_times.sort()
ans = 0
sum = 0
for i in _times:
    sum += i
    ans += sum
print(ans)