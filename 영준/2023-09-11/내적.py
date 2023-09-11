def solution(a, b):
    ab = [a[i] * b[i] for i in range(len(a))]
    answer = 0
    for num in ab:
        answer += num
    return answer