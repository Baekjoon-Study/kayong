M = int(input())
N = int(input())
data = []

for i in range(M, N+1):
    if i > 1: 
        is_prime = True
        for j in range(2, int(i/2) + 1):
            if i % j == 0:      # 부울대수를 활용해 전체 데이터가 조건문을 만족하지 않는 경우를 검출
                is_prime = False
                break
        if is_prime:
            data.append(i)

if data:                   #리스트 내 데이터가 있는지 확인
    print(sum(data))
    print(data[0])
else:
    print(-1)