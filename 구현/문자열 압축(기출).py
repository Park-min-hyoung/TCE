def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        temp = s[:step]
        cnt = 1
        for j in range(step, len(s), step):
            if s[j:j + step] == temp:
                cnt += 1
            else:
                if cnt > 1: compressed += str(cnt) + temp
                else: compressed += temp
                cnt = 1
                temp = s[j:j + step]

        if cnt > 1: compressed += str(cnt) + temp
        else: compressed += temp

        answer = min(answer, len(compressed))
    return answer

s = input()
print(solution(s))

# 틀렸음
'''나의 해결 : 아이디어는 비슷했지만 못푼것은 못푼거다'''
'''해결 아이디어
1. 문자열 길이의 반(1 ~ n / 2)까지만 체크해주면 된다(만약 문자열의 길이가 8일때 5까지 해주게되면 그것은 그냥 압축이 안되므로 8이다)
2. 단계별로 temp에 시작하는 원소를 담고 다음 원소와 비교를 해서 같으면 카운터를 올리고 틀리면 이제까지 압축됬던 문자열을 더해준 다음
카운터를 1로 초기화하고 temp를 수정해준다.
3. 마지막 문자 하나나 문자열은 안쪽 for문에서는 더해 줄 수 없으므로 안쪽 for문이 끝난 다음 더해주는 작업을 하고 단계별로 길이를 비교해서
바깥쪽 for문이 끝나면 리턴한다
4. 문자열을 더할 때 굳이 배열에 담는 방법 말고도 빈 문자열을 선언한 다음 하나씩 더해주는 방법도 있다. 그대신 바깥쪽 for문이 다시 시작되기 전에
체크해 주어야할 방도가 있어야 한다'''