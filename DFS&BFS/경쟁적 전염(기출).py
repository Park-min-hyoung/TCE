from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    virus, time, x, y = q.popleft()

    if time == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, x, y))

print(graph[target_x - 1][target_y - 1])

# 틀렸음
'''나의 해결 : 손도 대지 못했다'''
'''해결 아이디어
1. graph 리스트 변수에는 그래프 정보를 data 리스트 변수에는 바이러스의 정보를 저장한 후 정렬(숫자가 작은 것부터 점염하기 때문)
2. 방향을 나타내기 위해 dx, dy 변수 사용(중요, 자주 쓰인다)
3. 점염시간과 목표시간이 같으면 while문 탈출하게 만든다
4. popleft 메소드 사용 시 여러개의 값을 가져올 수 있다(튜플 형으로 저장된 값들)
5. 4방향 체크해서 벗어나지 않거나 0이면 바이러스를 점염시키고 큐에다가 점염된 곳의 정보를 삽입한다'''

'''문제
1. 시험관에 존재하는 모든 바이러스는 1초마다 상,하,좌,우로 증식(매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식)
(증식과정에서 특정한 칸에 이미 어떻나 바이러스가 존재한다면 그 곳에는 다른 바이러스가 들어갈 수 없다)
'''

'''입력
1. 1 ≤ 행 ≤ 200, 1 ≤ 열 ≤ 1,000'''

