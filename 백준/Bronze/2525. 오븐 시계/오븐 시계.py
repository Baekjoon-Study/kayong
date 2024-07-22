A, B = map(int, input().split())
C = int(input())
B += C
D = B // 60
if D > 0:
    A += D
    B %= 60
if A // 24 > 0:
    A %= 24
print(A, B)