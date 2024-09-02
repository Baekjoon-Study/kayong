n = int(input())
while n != -1:
    A = []                               #반복문에 변수 초기화 유념
    S = 0
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            A.append(i)
            S += i
    if S == n:
        print('%s = '%n, end='')
        for i in A:
            if i != A[len(A)-1]:
                print('%s + '%i, end='')
            else:
                print(i)
    else:
        print('%s is NOT perfect.'%n)
    n = int(input())