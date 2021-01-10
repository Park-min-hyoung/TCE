n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
sum = 0
temp = 0
for i in range(m):
    if temp < k:
        sum += num[n - 1]
        temp += 1
    else:
        sum += num[n - 2]
        temp = 0
print(sum)

'''시간 복잡도를 최소화하여 푸는 방법
n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

first = num[n - 1]
second = num[n - 2]

count = (m // k + 1) * k # 가장 큰 수가 더해진 횟수
count += m % (k + 1) # m이 k + 1로 나눠지지 않을 수 있는 경우도 있어서

result = 0
result += count * first
result += (m - count) * second

print(result)

1. 위의 예시처럼 최대 3번반복하고 더하는 횟수가 8이라고 하면 6665 6665 순으로 더해질 것이므로 
가장큰 수(6)이 나오는 횟수를 알아내면 된다.
2. 가장 큰수가 나오는 횟수를 알려면 먼저 몇번 반복되는지 알아야하므로 m(전체길이) // k + 1(반복횟수 + 1)를 구한 다음 k를 곱해주면 구할 수 있다.
3. count에 가장 큰수를 곱하면 되고 m - count에 그 다음으로 큰 수를 곱하면된다.
'''

