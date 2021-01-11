num = input()

sum = int(num[0])
for i in range(len(num) - 1):
    if int(num[i]) <= 1:
        sum += int(num[i + 1])
        continue
    sum *= int(num[i + 1])
print(sum)