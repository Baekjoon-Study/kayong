N = int(input())
num = input()
sum = 0
for i in range(len(num)):
    sum += ord(num[i]) - 48
print(sum)