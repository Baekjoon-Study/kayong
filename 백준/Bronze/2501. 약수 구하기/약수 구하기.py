N, K = map(int, input().split())
measure = [1]

for i in range(2, int(N/2) + 1):
    if N%i == 0:
        measure.append(i)
measure.append(N)        

if K > len(measure):
    print(0)
else:
    print(measure[K-1])