'''
- 1 : 대문자인경우 65 <= s <= 90
- 2 :소문자인경우 97 <= s <= 122
- 위 2가지 경우에서 +13일때 90과 122를 초과하는경우 -26
'''
import sys
input = sys.stdin.readline
ans = ""
for s in input().rstrip():
    if s.isupper():
        ans += chr((ord(s) - ord('A') + 13) % 26 + ord('A'))
    elif s.islower():
        ans += chr((ord(s) - ord('a') + 13) % 26 + ord('a'))
    else:
        ans += s
print(ans)
