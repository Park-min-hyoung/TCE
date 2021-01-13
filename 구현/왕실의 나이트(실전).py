night = input()

m = int(night[1])
n = ord(night[0]) - 96

mu = [[1, 2], [1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1], [-1, -2], [-1, 2]]

cnt = 0
for i in range(8):
    if 0 < m + mu[i][0] <= 8 and 0 < n + mu[i][1] <= 8:
            cnt += 1
print(cnt)