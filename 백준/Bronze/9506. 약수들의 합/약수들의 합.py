while True:
    n = int(input())
    if n == -1:
        break
    A = []
    S = 0
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            A.append(i)
            S += i
    if S == n:
        print(n, ' = ', ' + '.join(str(i) for i in A), sep='')
    else:
        print('%s is NOT perfect.'%n)