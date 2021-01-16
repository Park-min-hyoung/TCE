n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
info = []
for i in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulation():
    x, y = 1, 1 # 뱀의 현재 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 현재는 동쪽을 보고 있으므로 0
    time = 0
    index = 0 # 다음으로 회전해야 할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2 # 뱀이 이제부터 존재하므로
                q.append((nx, ny)) # 뱀이 차지하고 있는 공간을 늘린다
                px, py = q.pop(0) # 사과가 없다면 꼬리가 있는 위치를 뽑아내고
                data[px][py] = 0 # 꼬리가 없어졌으므로 뱀도 존재하지 않으므로 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulation())

# 틀렸음
'''나의 해결 : 손도 대지 못했다'''
'''해결 아이디어
1. n + 1 만큼의 판을 만들어 0에 대해서 편하게 하고 1을 넣어주고 시간에 의한 방향전환에 대한 배열을 만들어준다.
2. 동,남,서,북을 나타내는 배열을 만들고 오른쪽 또는 왼쪽으로 회전시 다음 방향을 direction으로 리턴하는 함수를 만들어 준다.
3. 현재 위치, 뱀이 차지하는 공간, 방향, 시간, 회전 여부, 꼬리의 여부를 나타내느 변수를 선언한다
4. nx, ny 변수를 통해 다음 위치를 저장하고 이것이 1이상 n미만의 공간에 있을때와 이것이 2가 아니면(2이면 겹친것이다) 다음위치로 이동한다
5. 사과가 없다면 뱀이 차지하는 공간을 넓혀주어야 하므로 뱀이 차지한 위치를 2로 수정해주고 뱀이 차지하고 있는 모든 공간에 대해 수정해준다
(차지하고 있는 공간에 대한 값을 2로 초기화 해줌으로써 나타낼 수 있고 q 배열을 통해 꼬리와 몸통을 구분할 수 있다)
6. 사과가 있다면 꼬리를 자를 필요없이 추가만 해주면 된다
7. 4번의 반대가 되면 시간을 카운터해주고 break 문을 걸어준다
8. 4번을 정상적으로 끝냈다면 x, y 좌표를 초기화해주고 카운터를 올려준다음 방향을 수정해준다
9. 너무 어렵다 너무 너무 너무 어렵다'''