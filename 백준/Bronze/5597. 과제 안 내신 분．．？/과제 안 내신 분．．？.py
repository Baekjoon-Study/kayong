std = list(range(1, 31))
for i in range(1, 29):
    num = int(input())
    std.remove(num)
print(min(std))
print(max(std))