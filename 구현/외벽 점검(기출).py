from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 길이를 2배로 늘린다
    for i in range(length):
        weak.append(weak[i] + n)
    # 최소 투입 인원을 구하기 위해서
    answer = len(dist) + 1

    # 0부터 length - 1 까지의 위치를 각각의 위치를 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점 부터 모든 취약 지점 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if weak[index] > position:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능 하다면 break
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if count > len(dist):
        return -1
    return answer

n = int(input())
weak = list(map(int, input().split()))
dist = list(map(int, input().split()))
print(solution(n, weak, dist))

# 틀렸음
'''나의 해결 : 손도 대지 못했다'''
'''해결 아이디어
1. 원형 문제 같은 경우는 길이를 2배로 해서 푸는것이 좋다
2. 친구들의 순열을 이용해서 2배로 늘려진 취약 지점 구간에서 시작점(밑에참고)을 두고 친구의 투입 수를 계산 해본다
3. 취약 구간이 2배로 늘려져서 길이는 len(weak) * 2이지만 시작점은 0 ~ len(weak)이다.
4. 하나의 순열의 원소를 이용해서 count를 올리고 만약 count가 친구의 수보다 많아지면 -1을 리턴한다
5. 시작점 선정 > 모든 순열 확인 > 하나의 순열의 원소 이용해 친구의 수 판별'''

'''
문제
1. 레스토랑의 구조는 완전히 둥그란 모양이고 외벽의 총 둘레는 N미터이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 취약한 지점들이 있다
2. 점검시간을 1시간으로 제한(친구들이 1시간 동안 이동할 수 있는 거리는 제각각 이므로 최소한의 친구들을 투입해 취약 지점을 점검하고
나머지는 내부 공사를 돕도록)
3. 레스토랑의 정북 방향 지머을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타낸다.
4. 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동
5. 외벽의 길이(N), 취약 지점의 위치가 담긴 배열(WEAK), 각 친구가 1시간 동안 이동할 수 있는 거리(dist)가 주어질때 취약 지점을 점검하기 위해
보내야 하는 친구 수의 최소값은??

주의사항
1. 1 <= n <= 200, 1 <= weak(부실 외벽 수) <= 15, 1 <= dist(친구 수) <= 8
2. 0 <= weak(원소) <= n - 1, 1 < = dist(원소) <= 100
3. 모두 투입해도 취약 지점 전부 점검할수 없는 경우 -1

풀이
1. 끝과 끝의 거리와 같은 dist의 원소가 있으면 그거 뽑아내면 되고 거리가 다르면 따로 처리해줘야 한다.
2. 그대로 하면 시계이고 배열을 뒤집으면 반시계
3. 시계일때와 반시계일때 구분해서 더작은 값을 answer로
'''