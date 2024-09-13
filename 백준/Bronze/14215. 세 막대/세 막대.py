a, b, c = map(int, input().split())

tri_legs = [a, b, c]
tri_legs.sort()

if tri_legs[2] >= tri_legs[0] + tri_legs[1]:
    tri_legs[2] = tri_legs[0] + tri_legs[1] - 1

print(sum(tri_legs))