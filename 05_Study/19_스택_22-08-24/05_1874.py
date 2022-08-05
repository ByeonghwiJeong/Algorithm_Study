'''
1 ~ n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있
8 
4 3 6 8 7 5 2 1
+ 1
+ 1 2
+ 1 2 3
+ 1 2 3 4
- 1 2 3 / 4
- 1 2 / 4 3 
+ 1 2 5 / 4 3
+ 1 2 5 6 / 4 3
- 1 2 5 / 4 3 6
+ 1 2 5 7 / 4 3 6
+ 1 2 5 7 8 / 4 3 6
- 1 2 5 7 / 4 3 6 8
- 1 2 5 / 4 3 6 8 7
- 1 2 / 4 3 6 8 7 5
- 1 / 4 3 6 8 7 5 2
- / 4 3 6 8 7 5 2 1
'''

import sys
input = sys.stdin.readline

def cal(index):
    global _nums, track, ans, _seq, pre_t
    if pre_t < target[index]:
        a = 0
        while True:
            if a == target[index]:
                break
            a = _seq.pop()
            _nums.append(a)
            ans.append('+')
        pre_t = target[index]
        return True
    else:
        t = _nums.pop()
        ans.append('-')
        if target[index] != t:
            print(t, target[i], pre_t)
            return False
        return True

N = int(input())
_seq = [i for i in reversed(range(1, N+1))]

target = []
for _ in range(N):
    target.append(int(input()))

_nums = []
track = []
ans = []
pre_t = 0

for i in range(2, N+1):
    flag = cal(i)
    if not flag:
        print('NO')
        break
else:
    print(*ans, sep='\n')
print(*ans, sep='\n')