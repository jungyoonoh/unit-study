#20220203
#프로그래머스(해시) : 위장
#https://programmers.co.kr/learn/courses/30/lessons/42578

#시간 초과 해결 못함

from itertools import combinations

def solution(clothes):
    answer = 0
    
    # 1개만 입을 때
    answer += len(clothes)
    
    for i in range(2,len(clothes)+1):
        result = list(combinations(clothes,i))
        count = 0

        # 같은 종류가 있는지 체크
        for j in result:
            same = []
            for k in range(len(j)):
                same.append(j[k][1]) #종류를 리스트에 담고
            if len(j) != len(set(same)): # 중복 체크
                count += 1 #중복이면 count++
        answer += len(result) - count  #전체 - 중복 개수
            
                 

    return answer