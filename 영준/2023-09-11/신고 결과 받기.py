def solution(id_list, report, k):
    rep = list(set(report)) # 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다. => 중복 제거가 나아 보임
    re_u = [user.split(' ')[0] for user in rep] # 신고자
    re_ed_u = [user.split(' ')[1] for user in rep] # 신고 당한 사람
    re_ed_u_count = {user:0 for user in re_ed_u} # 신고 당한 횟수
    re_ed_k = [] # 신고가 k회 이상인 경우 신고 당한 유저를 넣을 list
    mail = {user:0 for user in id_list} # 메일 받은 횟수
    
    # 신고 당한 횟수를 정리
    for user in re_ed_u:
        re_ed_u_count[user] += 1
        if re_ed_u_count[user] == k:
            re_ed_k.append(user)
    
    # 메일을 받을 유저를 dictionary에 += 1로 한다.
    for user in re_ed_k:
        for i in range(len(re_ed_u)):
            if user == re_ed_u[i]:
                mail[re_u[i]] += 1
    
    # 메일 받은 횟수를 넣어야 하므로 values를 가져온다.
    answer = list(mail.values())
    return answer