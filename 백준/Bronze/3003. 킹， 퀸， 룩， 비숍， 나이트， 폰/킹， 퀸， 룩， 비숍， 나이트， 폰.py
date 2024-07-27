chess = list(map(int, input().split()))
plus = []
for i in range(len(chess)):
    if i == 0 or i == 1:
        plus.append(1-chess[i])
    elif i > 1 and i < 5:
        plus.append(2-chess[i])
    else:
        plus.append(8-chess[i])
    print(plus[i], end=' ')