'''
< Longest Subarray >

a = [1, 2, 3], k=3
1, 2, 3, 12, 23, 123
12 >> 최대길이 2 return

a = [3, 1, 2, 1], k=4
3, 1, 2, 1, 31, 12, 21, 312, 121, 321
121 >> 최대길이 3 return

0 3 4 6 7
l = 0, r = 1
sum = 3
l = 0, r = 2
sum = 4
l = 0, r = 3
sum = 6 > k
l = 1, r = 3
sum = 3
l = 1, r = 4
sum = 4, r - l 저장
l = 1, r = 5
- r이 index out of range 종료
'''

def maxLength(a, k):
    # Write your code 
    presum = [0]
    for i in a:
        presum.append(presum[-1] + i)
    ret = 0
    l = 0
    r = 1
    while l < r:
        print(l, r)
        if r == len(a) + 1: break
        _sum = presum[r] - presum[l]
        if _sum > k:
            l += 1
        else:
            ret = max(ret, r - l)
            r += 1
    return ret

print(maxLength([3, 1, 2, 1], 4))