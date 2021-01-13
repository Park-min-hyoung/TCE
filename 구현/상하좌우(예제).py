num = int(input())
vector = list(input().split())

m = 1
n = 1
for i in range(len(vector)):
    if vector[i] == 'R':
        if n + 1 <= num: n += 1
    elif vector[i] == 'L':
        if n - 1 > 0: n -= 1
    elif vector[i] == 'U':
        if m - 1 > 0: m -= 1
    else:
        if m + 1 <= num: m += 1
print(m, n)