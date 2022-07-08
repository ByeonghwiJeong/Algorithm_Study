import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

def reverse(x):
  new_x = str(x)[::-1]

def isPrime(x):
  if x == 1:
    return False
# num이 100같은 수가 넘어와서 x에 1이들어갈경우 고려
  for i in range(2,x):
    if x % i == 0:
      return False
  return True

for num in nums:
  tmp = reverse(num)
  if isPrime(tmp) == True:
    print(tmp, end=' ')