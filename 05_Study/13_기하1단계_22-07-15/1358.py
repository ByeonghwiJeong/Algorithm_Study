'''
x**2 + (y-radius)**2 <= radius**2
(x-width)**2 + (y-radius)**2 <= radius**2
X <= x <= X+width
Y <= y <= Y+height
'''
import sys
input = sys.stdin.readline

def check_in(W, H, X, Y, x, y):
    if Y <= y <= Y + H:
        if (x - X)**2 + (y - H/2 - Y)**2 <= (H/2)**2 \
             or (x - X - W)**2 + (y - H/2 - Y)**2 <= (H/2)**2 \
                 or X <= x <= X + W:
            return 1
    return 0

W, H, X, Y, P = map(int, input().split())
ans = 0
for _ in range(P):
    x, y = map(int, input().split())
    ans += check_in(W, H, X, Y, x, y)

print(ans)