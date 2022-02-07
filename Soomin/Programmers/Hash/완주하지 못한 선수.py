#20220201
#프로그래머스(해시) : 완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''

    #이름 순으로 정렬 후 바로바로 비교해주는 것이 더 빠름
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
            exit(0)
        #이름 순 마지막 사람이 완주하지 못했을 경우
        elif i==len(completion)-1:
            answer = participant[i+1]
            return answer

    # "in, not in" 쓰면 시간 초과
    # for p in participant:
    #     if p in completion:
    #         completion.remove(p)
    #     else:
    #         answer = p
    #         return answer
    #         exit(0)