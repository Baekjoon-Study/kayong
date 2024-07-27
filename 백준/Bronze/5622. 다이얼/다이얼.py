W = input()
cnt = 0
for i in range(len(W)):
    asci = ord(W[i])
    if asci >= 65 and asci < 68:
        cnt += 3
    elif asci >= 68 and asci < 71:
        cnt += 4
    elif asci >= 71 and asci < 74:
        cnt += 5
    elif asci >= 74 and asci < 77:
        cnt += 6
    elif asci >= 77 and asci < 80:
        cnt += 7
    elif asci >= 80 and asci < 84:
        cnt += 8
    elif asci >= 84 and asci < 87:
        cnt +=  9
    elif asci >= 87 and asci < 91:
        cnt += 10
print(cnt)
        