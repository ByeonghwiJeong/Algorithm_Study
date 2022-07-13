import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  chs = input().strip() #strip()안붙이면 enter인식
  stk = []
  isVPS = True
  for ch in chs:
    if ch == '(':
      stk.append(ch)
    else:
      if len(stk) > 0: 
        # if stk: 이런식으로 가능 
        stk.pop()
      else:
        isVPS = False
        break

  if stk: 
    isVPS = False

  print('YES' if isVPS else 'NO')
    
  