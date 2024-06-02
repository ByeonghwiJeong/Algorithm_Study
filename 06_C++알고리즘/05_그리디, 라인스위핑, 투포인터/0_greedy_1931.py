import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0
for s, e in time:
    if s < end_time:
        continue
    cnt += 1
    end_time = e
print(cnt)