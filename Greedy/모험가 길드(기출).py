n = int(input())
men = list(map(int, input().split()))
men.sort()

temp = 0
cnt = 0
for i in range(len(men)):
    temp += 1
    if temp >= men[i]:
        cnt += 1
        temp = 0
print(cnt)