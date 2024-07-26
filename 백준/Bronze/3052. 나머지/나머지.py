A = []
for i in range(10):
    num = int(input())
    num %= 42
    if len(A) == 0:
            A.append(num)
    for j in range(len(A)):
        if A[j] == num:
            break
        if j == len(A)-1:
            A.append(num)
print(len(A))