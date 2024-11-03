N, M = map(int, input().split())
Card_list = list(map(int, input().split()))

res = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            chk = Card_list[i] + Card_list[j] + Card_list[k]
            if chk <= M:
                res = max(res, chk)

if res != 0:
    print(res)
else:
    print("더 큰 M이 필요")
