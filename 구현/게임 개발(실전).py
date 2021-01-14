m, n = map(int, input().split())
mc, nc, d = map(int, input().split())
cboard = [[0] * n for _ in range(m)]
board = [[int(x) for x in input().split()]for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 0
turn_cnt = 0
while True:
    turn_left()
    nx = mc + dx[d]
    ny = nc + dy[d]
    if board[nx][ny] == 0 and cboard[nx][ny] == 0:
        cboard[nx][ny] = 1
        cnt += 1
        mc = nx
        nc = ny
        turn_cnt = 0
        print(mc, nc)
        continue
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        nx = mc - dx[d]
        ny = nc - dy[d]
        if board[nx][ny] == 0:
            mc = nx
            nc = ny
        else:
            break
        turn_cnt = 0

print(cnt)

# 틀렸음
'''나의 해결 : 손도 대지 못했다.'''
'''해결 아이디어
1. 간곳을 체크하기 위해 0으로 초기화 되어있는 똑같은 크기의 판을 따로 만든다(나는 원래 판에서 수정하려고 했다)
2. 방향문제 같은 경우는 m과 n따로 배열로 정리해두는게 문제풀때 유용하다
3. 왼쪽으로 회전하는 함수를 생성한다(-1씩 빼주면 다음 방향으로 간다, 단 북에서 서로갈때는 3이 나와야하므로 -1에서 3으로 수정해줘야 한다)
4. 방문횟수와 회전횟수의 변수를 생성한후에 trun_left 함수를 호출함으로써 작업을 시작한다
5. 방향에 해당하는 값을 더해줘서 0이면은 m,n초기화 및 cboard배열 초기화 cnt 증가 turn_cnt를 0으로 초기화하고 만약 바다이거나 이미 가본곳이면
turn_cnt만 +1 해준다
6. 만약 trun_cnt가 4라면(다돌았을때) 뒤로 가는데 만약 0이라면 뒤로감으로써 m,n을 초기화해주고 1이라면 break문을 걸어준다
turn_cnt는 다시 0으로 초기화 된다'''