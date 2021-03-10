n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출(어차피는 A는 커지는데 B는 작아지므로 교체하면 바보 짓이다)
        break

print(sum(A))