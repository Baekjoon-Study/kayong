S = input()
lst = list(S)
for i in range(97, 123):
    if lst.count(chr(i)) > 0:
        print(lst.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')