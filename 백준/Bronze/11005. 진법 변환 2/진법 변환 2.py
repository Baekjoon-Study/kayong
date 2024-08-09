N, B = map(int, input().split())
lst = []
while N > 0:
    lst.append(N%B)
    N = N//B
lst.reverse()

t = ''
for i in range(len(lst)):
    if lst[i] >= 10:
        t += chr(lst[i]+55)
    else:
        t += chr(lst[i] + 48)

print(t)