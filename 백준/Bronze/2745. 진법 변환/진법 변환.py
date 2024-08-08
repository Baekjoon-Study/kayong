N, B = input().split()
B = int(B)

res = 0
for index, char in enumerate(reversed(N)):
    if '0' <= char <= '9':
        value = int(char)
    else:
        value = ord(char) - 55
    res += value*B**index

print(res)