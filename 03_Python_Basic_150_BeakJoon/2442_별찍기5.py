N = int(input())
for i in range(N):
    length = N * 2 - 1
    star_num = 1 + 2 * i
    side_space = (length - star_num) // 2 
    s = ' '* side_space + '*' * star_num
    print(s)
# for i in reversed(range(N-1)):
#     length = N * 2 + 1
#     star_num = 1 + 2 * i
#     side_space = (length - star_num) // 2 
#     s = ' '* side_space + '*' * star_num + ' ' * side_space
#     print(s)