def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if board[x][y] == 0:
        board[x][y] = 1
        dfs(x, y + 1) # 오른쪽
        dfs(x - 1, y) # 위쪽
        dfs(x, y - 1) # 왼쪽
        dfs(x + 1, y) # 아래쪽
        return True
    return False


n, m = map(int, input().split())

board = [[int(x) for x in input().split()]for _ in range(n)]
result = 0

for x in range(n):
    for y in range(m):
        if dfs(x, y) == True:
            result += 1

print(result)

'''
접근
1. 이중 배열을 통해 원소를 식별
2. 해당 원소가 0이면 1로 바꾸고 인접해있는 원소를 하나씩 방문해 0이면 1로 바꾸고 그렇지 않으면 그냥 넘어간다(완전탐색 인가?)
'''