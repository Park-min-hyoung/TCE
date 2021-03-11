import sys

n = int(input())
data = list(map(int, input().split()))
m_data = max(data)

hause = [0] * (m_data + 1)
for i in data:
    hause[i] += 1

before_distance = sys.maxsize
after_distance = 0
target = 0
for i in range(1, len(hause)):
    if hause[i] >= 1:
        for j in range(1, len(hause)):
            if hause[j] >= 1:
                after_distance += (abs(i - j) * hause[j])
    if after_distance != 0:
        if before_distance > after_distance:
            target = i
            before_distance = after_distance
            after_distance = 0

print(target)

''' 동빈님 소스코드
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값을 출력(무조건 중간에 있는 값이 가장 작다
print(data[(n - 1) // 2])
'''

'''문제
1. 특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정, 효율성을 위해 안테나로부터 모든 집까지의 거리가 최소가 되도록 설치
2. 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다
'''