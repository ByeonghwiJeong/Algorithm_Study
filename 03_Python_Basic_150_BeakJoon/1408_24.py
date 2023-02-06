A = list(map(int, input().split(':')))
B = list(map(int, input().split(':')))

tmp_s = B[2] - A[2]
if  tmp_s < 0:
    tmp_s += 60
    tmp_m = B[1] - A[1] - 1
else:
    tmp_m = B[1] - A[1] 

if tmp_m < 0:
    tmp_m += 60
    tmp_h = B[0] - A[0] -1
else:
    tmp_h = B[0] - A[0]

if tmp_h < 0:
    tmp_h += 24

ans = [tmp_h, tmp_m, tmp_s]
ans = ['0'+str(x)  if len(str(x)) == 1 else str(x) for x in ans]
print(':'.join(ans))
