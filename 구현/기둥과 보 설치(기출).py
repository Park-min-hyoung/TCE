def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥이라면
            # y좌표가 0 또는 기둥이 보의 양쪽끝에 있을때 또는 기둥 위에 있을때
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 기둥이 이상하다면 False 반환
        if stuff == 1: # 보라면
            # 보의 양쪽끝 중 하나가 기둥위에 있을때 또는 보의 양쪽끝이 동시에 보와 연결되어 있을때
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 기둥이 이상하다면 False 반환

    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operation = frame
        if operation == 0: # 삭제
            answer.remove([x, y, stuff]) # 일단 삭제해보고
            if not possible(answer): # 구조가 이상하다면
                answer.append([x, y, answer]) # 다시 설치
        if operation == 1: # 설치
            answer.append([x, y, stuff]) # 일단 설치해보고
            if not possible(answer):
                answer.remove([x, y, stuff]) # 다시 삭제

    return sorted(answer) # 배열을 정렬

n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
print(solution(n, build_frame))

# 틀렸음
'''나의 해결 : 틀렸음 예제는 맞췄는데 접근 방식이 아예달랐음'''
'''해결 아이디어
1. possible 메소드를 통해 기둥을 설치하거나 삭제할때 조건을 통해 보았을 때 이상하다면 False를 반환하고 괜찮으면 True를 반환
2. 삭제 같은 경우 기둥이나 보를 삭제하고 possible 메서드로 체크를 해보고 괜찮으면 그대로 두고 이상하면 원상복구한다
3. 설치 같은 경우 기둥이나 보를 설치하고 possible 메서드로 체크를 해보고 괜찬으면 그대로 두고 이상하면 원상복구한다.
4. 구현 문제는 시뮬레이션 또는 완전 탐색 이 문제 같은 경우는 시뮬레이션 문제이다'''