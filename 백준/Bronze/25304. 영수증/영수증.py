X = int(input())
N = int(input())
P = 0
for i in range(N):
    a, b = map(int, input().split())
    P += a*b
if X == P:
    print('Yes')
else:
    print('No')