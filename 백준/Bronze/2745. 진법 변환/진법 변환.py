N, B = input().split()
Bb = int(B)
Nn = list(N)

N_dict = {}
for i in range(26):
    a = chr(65+i)
    N_dict[a] = 10+i

res = 0    
for i in range(len(Nn)):
    if ord(Nn[i]) >= 65 and ord(Nn[i]) <= 90:
        Nn[i] = N_dict[Nn[i]]
    else:
        Nn[i] = int(Nn[i])
    res += Nn[i]*Bb**(len(Nn)-1-i)
    
print(res)