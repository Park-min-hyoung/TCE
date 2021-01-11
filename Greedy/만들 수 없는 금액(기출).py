n = int(input())

coin = list(map(int, input().split()))
coin.sort()

target = 1
for i in n:
    if target < i:
        break
    else:
        target += i
print(target)

'''나의 해결: 맞긴 맞은거 같은데 while문과 for문을 같이 사용하므로 시간복잡도에 있어서 좋지 않은 프로그램이다'''
'''해결 아이디어
1. 양의 정수라고 했으므로 target = 1로 정해주고 target이 오름차순으로 정렬된 원소보다 크거나 같으면 target에 원소를 더해줘서 업테이트한다.
2. target이 작으면 더 이상 만들 재료가 없으므로 break를 걸어준다'''