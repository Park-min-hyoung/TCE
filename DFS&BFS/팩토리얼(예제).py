def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= (i + 1)

    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

inpu = int(input())
print('반복적으로 구현: ', factorial_iterative(inpu))
print('재귀적으로 구현: ', factorial_recursive(inpu))