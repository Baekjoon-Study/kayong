A = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            A[x+i][y+j] = 1
            
cnt = 0
for p in range(100):
    for q in range(100):
        if A[p][q] == 1:
            cnt += 1
    
print(cnt)       