def MakeMatrix(m, n):
    for i in range(n):
        ele = list(map(int, input().split()))
        m.append(ele)
    return m

def printSumMatrix(a, b):
    for i in range(N):
        for j in range(M):
            print(A[i][j] + B[i][j], end=' ')
        print()

N, M = map(int, input().split())
A, B = [], []
AA = MakeMatrix(A, N)
BB = MakeMatrix(B, N)
printSumMatrix(AA, BB)