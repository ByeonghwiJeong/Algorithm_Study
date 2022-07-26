'''
1. 근처에 보이는 숫자 N개를 종이에 적는다.
2. 그 다음, 종이에 적은 수를 M으로 나누었을때, 
    나머지가 모두 같게 되는 M을 모두 찾으려고 한다. 
3. M을 모두찾는 프로그램

입력)
    - 첫번째 줄에 종이레 적은 수의 개수 N이 주어진다.
'''
import sys
input = sys.stdin.readline

def gcd(x, y):
    z = x % y
    if z == 0:
        return y
    return gcd(y, z)

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

minus_nums = [nums[i] - nums[i-1] for i in range(1, N)]
_gcd = minus_nums[0]
for i in range(1, N-1):
    _gcd = gcd(_gcd, minus_nums[i])

result = [_gcd]

# 시간 복잡도 >>> O(N)
# for i in range(2, _gcd + 1):
#     if _gcd % i == 0:
#         result.append(i)

# < _gcd의 약수 구하기 >
for i in range(2, int(_gcd**(1/2))+1):
    if _gcd % i == 0:
        result.append(i)
        if i**2 != _gcd:
            result.append(_gcd // i)
# 시간 복잡도 >>> O(N^(1/2))

result.sort()
print(*result, sep=' ')