#20220202
#프로그래머스(정렬) : H-Index
#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort(reverse = True)
        # count = 0
    for i in citations:
        count = 0
        for j in range(len(citations)):
            if i <= citations[j]:
                count += 1
        # 제일 큰 수가 0일 때 == 0밖에 없을 때        
        if citations[0] == 0:
            answer = 0 
            
        elif count > i:
            print(i)
            answer = count -1
            return answer
            exit(0)
    
        else:
            answer = count
            
            
    
    return answer