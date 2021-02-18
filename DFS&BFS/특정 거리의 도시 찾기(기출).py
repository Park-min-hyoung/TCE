from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


'''조건
1. 2 <= 도시의 수 <= 300,000, 1 <= 도로의 개수 <= 1,000,000, 1 <= 거리 정보 <= 1,000,000, 1 <= 출발 도시 <= 도시의 수'''

# 틀렸음
'''나의 해결 : 손도 대지 못했다'''
'''해결 아이디어
1. 각 입력값을 받아주고 숫자를 구분하기 쉽게 n개의 도시가 있다면 n + 1개의 도시가 있는 그래프를 만들어 준다
2. 모든 도시에 대한 최단 거리 또한 n + 1개로 해준다음 -1로 초기화하고 출발도시는 0으로 초기화 한다
3. BFS를 이용해 현재 도시를 큐에서 뽑아낸 다음 인접해 있는 도시의 거리 값이 -1이면 값을 초기화해주고 큐에 도시 번호를 추가해준다.
4. check = False 부울 변수를 통해 최단 거리가 k인 graph의 원소가 있다면 출력해준다음 check를 True로 수정하고 한개도 없다면
check = False 조건을 통해 -1을 출력한다'''