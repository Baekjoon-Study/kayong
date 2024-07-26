N, M = map(int, input().split())
A = list(range(1, N+1))
for k in range(M):
    i, j = map(int, input().split())
    while i < j:
        A[i-1], A[j-1] = A[j-1], A[i-1]
        i += 1
        j -= 1
for p in A:
    print(p, end=' ')