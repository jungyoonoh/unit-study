# 프로그래머스 완주하지 못한 선수

from collections import defaultdict


def solution(participant, completion):
    dic = defaultdict(int)
    for i in participant:
        dic[i] += 1
    for j in completion:
        dic[j] -= 1
        if dic[j] == 0:
            dic.pop(j)
    return ''.join(list(dic.keys()))
