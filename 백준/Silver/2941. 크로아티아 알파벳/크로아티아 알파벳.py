S = input()
i, cnt = 0, 0

while i < len(S):
    a = S[i]
    if a == 'c' and i+1 < len(S) and (S[i+1] == '=' or S[i+1] == '-'):
        i += 1
    elif a == 'd' and i+2 < len(S) and S[i+1] == 'z' and S[i+2] == '=':
        i += 2
    elif a == 'd' and i+1 < len(S) and S[i+1] == '-':
        i += 1
    elif i+1 < len(S) and S[i+1] == 'j' and (a == 'l' or a == 'n'):
        i += 1
    elif i+1 < len(S) and S[i+1] == '=' and (a == 's' or a == 'z'):
        i += 1
    cnt += 1
    i += 1
    
print(cnt)