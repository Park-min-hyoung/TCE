from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []
for r in range(n):
    data = list(map(int, input().split()))

    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0

    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp

    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)

# 틀렸다
'''나의 해결 : 틀렸다 고집 부리다가 시간만 날렸다 다음 부터는 그냥 시간 다 사용했으면 답지 보자 고집피우지 말고 그리고
너느 0%야 제발 귀찮더라도 다른거 참고하자'''
''' 해결 아이디어
1. 먼저 배열중에 집과 치킨집을 구분하여 배열에 집어 넣는다
2. 조합 라이브러리를 통해 조합 리스트를 만든다
3. 치킨 거리의 합을 구하는 메소드를 작성한다
4. 치킨 조합 리스트를 순회하면서 치킨 거리의 합 메소드를 통해 최소 거리를 찾아낸다
5. 예를 들어 5집이 있고 10개의 조합이 있다면 5집이 1번 조합에 들어가서 거리의 합을 구하는것이 3번 메소드이고
모든 조합 번호에 3번 메소드를 적용하는 것이 4번 메소드이다(조합 리스트 다 방문해서 가장 작은 값)'''