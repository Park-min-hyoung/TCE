n = input()
harf = len(n) // 2

sum = 0
for i in range(len(n)):
    if i < harf:
        sum += int(n[i])
    else:
        sum -= int(n[i])
if sum == 0: print("LUCKY")
else: print("READY")