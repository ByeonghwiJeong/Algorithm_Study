from bisect import bisect_right, bisect_left
x = [0, 2, 5 ,5 , 10]
print('3l', bisect_left(x, 3)) #2
print('3r', bisect_right(x, 3)) #2
print('5l', bisect_left(x, 5)) #2 
print('5r', bisect_right(x, 5)) #4
print('0l', bisect_left(x, 0)) #
print('0r', bisect_right(x, 0))
print('10l', bisect_left(x, 10)) #
print('10r', bisect_right(x, 10))

