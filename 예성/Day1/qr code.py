def solution(q, r, code):
    temp = []
    for i in range(len(code)):
        # print(code[i::q])
        temp.append(code[i::q])  # q 크기의 스텝으로 나누어 부분 문자열을 추출
    return temp[r]

