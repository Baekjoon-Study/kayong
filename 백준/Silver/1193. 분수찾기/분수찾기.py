X = int(input())

S_num = 1

cnt = 1

while cnt < X:

    S_num += 1

    cnt += S_num

a =  X - (cnt - S_num)

b = S_num + 1 - a

if S_num % 2 == 1:

    a, b = b, a

print('%s/%s'%(a, b))

