x1, y1 = map(int, input().split())       
x2, y2 = map(int, input().split())       
x3, y3 = map(int, input().split())       
if x1 != x2 and y1 != y2:
    ans_x = x1 + x2 - x3
    ans_y = y1 + y2 - y3
elif x1 != x3 and y1 != y3:
    ans_x = x1 + x3 - x2
    ans_y = y1 + y3 - y2
elif x2 != x3 and y2 != y3:
    ans_x = x2 + x3 - x1
    ans_y = y2 + y3 - y1
print(ans_x, ans_y)
'''
2개 있는값이 아닌 1개 있는 값을 찾자
'''