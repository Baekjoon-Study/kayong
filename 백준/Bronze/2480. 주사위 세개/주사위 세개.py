A, B, C = map(int, input().split())
if A == B and B == C:
    print(10000 + A*1000)
elif A != B and B != C and C != A:
    print(max(A, B, C)*100)
else:
    if A == B:
        D = A
    elif A == C:
        D = A
    else:
        D = B
    print(1000 + D*100)