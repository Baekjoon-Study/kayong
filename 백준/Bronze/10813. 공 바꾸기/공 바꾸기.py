N, M = map(int, input().split())
A = list(range(1, N+1))
for i in range(M):
    i, j = map(int, input().split())
    A[i-1], A[j-1] = A[j-1], A[i-1]
for k in A:
    print(k, end=' ')
    