def factorial(i):
    if i == 0:
        return 1
    else:
        answer = i * factorial(i - 1)
        return answer


def solution(n):
    for i in range(1, 20):
        if factorial(i) > n:
            return i-1
