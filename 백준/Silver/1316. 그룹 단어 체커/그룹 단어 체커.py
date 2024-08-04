def isGroup(s):
    seen = set()
    prev = ''
    for i in s:
        if i != prev:
            if i in seen:
                return False
            seen.add(i)
        prev = i
    return True

N = int(input())
cnt = 0

for _ in range(N):
    S = input()
    if isGroup(S):
        cnt += 1

print(cnt)