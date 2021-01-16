def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotate in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

# 틀렸음
'''나의 해결 : 손도 못댔다'''
'''해결 아이디어
1. 먼저 90도 돌리는 함수, 확장된 열쇠의 중간 부분이 모두 1인지 체크하는 함수, 솔루션 함수를 각각 만들어야 한다
2. 2차원 배열을 90도 돌리는 함수는 팀노트를 참고
3. 확장된 배열의 중간 부분이 모두 1인지 체크 하기 위해서는 3배 확장 시켰으므로 3으로 나눈다음 변수에 넣고 반복문은 변수의 수에서 변수에 수 * 2까지 돌림으로써
중간의 좌물쇠가 모두 1인지 확인 할 수 있다
4. 기존 자물쇠를 3배 확장한 다음 중간 부분에 기존 좌물쇠의 값을 넣는다
5. 4방향을 체크해줘야 한다. 그러므로 반복문마다 배열을 90도 돌려준다음 한 칸씩 이동하면서 열쇠를 자물쇠에 넣은 다음 check 함수로 확인한 후
모두 1이면 True를 반납하고 만약 아니면 좌물쇠에서 열쇠를 빼는 연산을 수행하고 계속 반복한다
6. 어렵다 진짜 여럽다 이게 쉬운거라는데 나는 그저 예시에 나온 입력만 충족 시키면 되는 줄 알았는데 아니었다
배열을 돌릴 줄도 모르고, 확장 시킬줄도 모르고, 한칸씩 넣어보자는 아이디어도 내지 못했고, 확인할 줄도 몰랐고, 열쇠를 자물쇠에서 다시 뺀다는 생각조차
못했다.
7. 좌물쇠 확장 > 열쇠 90도 회전 > 한칸씩 넣어보기 > 확인 > (성공시 : 끝, 실패시 : 열쇠 뽑고 다시 반복) > 다시 열쇠 90도 회전'''