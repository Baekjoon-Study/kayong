N = int(input())
std = 1
T = 6
cnt = 1

while N > std:
    std += T
    T += 6
    cnt += 1

print(cnt)