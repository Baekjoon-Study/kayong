def Big_0_check(A1, A0, C, N0):
    check = 0
    if C > A1:
        check = point_check(A1, A0, C, N0)
    elif C == A1:
        check = point_check(A1, A0, C, N0)
    return check

def point_check(A1, A0, C, N0):
    if A1*N0 + A0 <= C*N0:
        return 1
    else:
        return 0

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(Big_0_check(a1, a0, c, n0))