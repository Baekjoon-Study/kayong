A = [input() for _ in range(5)]
t = ''

for i in range(15):
    for j in A:
        if i < len(j):
            t += j[i]
            
print(t)