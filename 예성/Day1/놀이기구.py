def solution(price, money, count):
    cur = 0
    for i in range(1, count+1):
        cur += price * i
    result = cur - money
    if result >= 0:
        return result
    else:
        return 0
