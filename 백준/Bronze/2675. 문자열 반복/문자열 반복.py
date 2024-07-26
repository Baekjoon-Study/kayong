T = int(input())
for i in range(T):
    R, S = input().split()
    P = ''
    for j in range(len(S)):
        for k in range(ord(R)-48):
            P += S[j]
    print(P)