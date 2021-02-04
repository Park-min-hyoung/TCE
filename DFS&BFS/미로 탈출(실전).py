from collections import deque

def bfs(x, y):
    result = 1
    queue1 = deque(x)
    queue2 = deque(y)

    while deque:
        vx = queue1.popleft()
        vy = queue2.popleft()
        if vx == n - 1 and vy == m - 1:
            result += 1
            break

        graph[vx][vy] = 0
        if graph[vx - 1][vy] == 1:
            queue1.append(vx - 1)
            queue2.append(vy)
        if graph[vx + 1][vy] == 1:
            queue1.append(vx + 1)
            queue2.append(vy)
        if graph[vx][vy - 1] == 1:
            queue1.append(vx)
            queue2.append(vy - 1)
        if graph[vx][vy + 1] == 1:
            queue1.append(vx)
            queue2.append(vy + 1)
        result += 1

    return result


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(bfs(0, 0))

