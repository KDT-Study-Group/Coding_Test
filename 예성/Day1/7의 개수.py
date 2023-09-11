def solution(array):
    str1 = ''.join(str(s) for s in array)
    cnt = 0

    for i in range(len(str1)):
        if str1[i] == '7':
            cnt += 1
    return cnt