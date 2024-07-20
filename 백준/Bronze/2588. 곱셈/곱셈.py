A = int(input())
B = int(input())
B1 = B % 10
print(A * B1)
B2 = (B % 100) // 10
print(A * B2)
B3 = B // 100
print(A * B3)
print((A*B1) + 10*(A*B2) + 100*(A*B3))