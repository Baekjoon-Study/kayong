Score_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
SumScore = 0
SumTime = 0

for _ in range(20):
    A, B, C = input().split()
    B = float(B)
    if C != 'P':
        SumTime += B
        SumScore += B * Score_dict[C]

print(SumScore / SumTime)
