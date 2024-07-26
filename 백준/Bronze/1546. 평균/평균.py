N = int(input())
A = list(map(int, input().split()))
M = max(A)
Sum = 0
for i in range(len(A)):
    A[i] = A[i]/M*100
    Sum += A[i]
print(Sum/len(A))