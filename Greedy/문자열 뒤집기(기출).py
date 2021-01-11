n = input()

cnt = 0
for i in range(1, len(n)):
    if n[i - 1] != n[i]:
        cnt += 1

if cnt % 2 == 0: print(cnt // 2)
else: print(cnt // 2 + 1)