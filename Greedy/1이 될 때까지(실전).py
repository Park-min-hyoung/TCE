n, k = map(int, input().split())

cnt = 0
while n > 1:
    if n % k == 0:
        cnt += 1
        n //= k
        continue
    cnt += 1
    n -= 1
print(cnt)