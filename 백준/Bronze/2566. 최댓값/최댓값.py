A = []
for i in range(9):
    column = list(map(int, input().split()))
    A.append(column)

Max, n, m = 0, 0, 0
for j in range(9):
    for k in range(9):
        if A[j][k] > Max:
            n, m = j, k
            Max = A[j][k]
print(Max)
print(n+1, m+1)