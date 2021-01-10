n, m = map(int, input().split())
card = [[int(x) for x in input().split()]for _ in range(n)]

mi = 0
for i in range(n):
    min_value = min(card[i])
    mi = max(mi, min_value)
print(mi)