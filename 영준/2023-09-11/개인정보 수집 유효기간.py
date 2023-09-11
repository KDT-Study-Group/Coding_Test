def date_convert(time): # 연도와 월을 전부 일수로 변경한다.
    year, month, day = map(int, time.split('.'))
    return year * 12 * 28 + month * 28 + day # 1달이 28일로 나와 있음

def solution(today, terms, privacies):
    term_dict = dict() # 빈 dictionary 생성 => 약정을 일수로 변경해서 넣기 위해 생성
    today = date_convert(today) # 약정이 시작한 날을 일수로 변경
    answer = []
    
    # 약정 기간을 전부 일수로 변경
    for term in terms :
        name, period = term.split()
        term_dict[name] = int(period) * 28
    
    # 해당 약정에 한해서 조건에 해당하는 경우의 번호를 넣는다.
    for i, privacy in enumerate(privacies) :
        start, name = privacy.split()
        end = date_convert(start) + term_dict[name]
        if end <= today :
            answer.append(i+1)
    
    return answer