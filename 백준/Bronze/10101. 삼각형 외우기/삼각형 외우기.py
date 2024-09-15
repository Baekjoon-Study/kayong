tri_angle = []
for _ in range(3):
    angle = int(input())
    tri_angle.append(angle)

if sum(tri_angle) != 180:
    print("Error")
else:
    same_angle_num = len(set(tri_angle))
    if same_angle_num == 1:
        print("Equilateral")
    elif same_angle_num == 2:
        print("Isosceles")
    else:
        print("Scalene")