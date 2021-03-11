n = int(input())

student = []
for i in range(n):
    student.append(input().split())

# student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
student = sorted(student, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])

'''문제
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점소가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로'''