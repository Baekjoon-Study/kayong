def Delsort(s):
    t = ''
    for i in range(len(s)):
        if i + 1 < len(s):
            if s[i+1] != s[i]:
                t += s[i]
        else:
            t += s[i]
    return t

N = int(input())
cnt = 0
for _ in range(N):
    S = input()
    S1 = Delsort(S)
    S2 = Delsort(''.join(sorted(S1)))
    if len(S1) == len(S2):
        cnt += 1

print(cnt)