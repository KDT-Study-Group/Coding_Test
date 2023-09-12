'''
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
'''

def solution(n):
    try:
        if isinstance(n, int) and n > 0 and n <= 10000: # isinstance(n, int): n이 정수인지 확인해주는 함수.
            result = ""
            for i in range(n):
                if i%2==0:
                    result += '수'
                else:
                    result += '박'
            return result
        else:
            raise ValueError("n은 1 이상 10,000 이하의 자연수여야 합니다.")
    except Exception as e:
        return str(e)

result = solution(11)
print(result)