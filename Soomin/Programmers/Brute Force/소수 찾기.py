#20220202
#프로그래머스(완전탐색) : 소수찾기
#https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    num = list(numbers)
    nump = []
    answer = 0
    
    for i in range(len(num)):
        result = list(permutations(num,i+1))
        nump.append([''.join(j) for j in result]) #'17','117' 이 형태로 저장하는 방법
    
    nump = list(set(sum(nump,[])))
    #set은 nump[0] <- 이렇게 불가! list나 tuple로 변경해서 사용하기

    nump = list(set(list(map(int, nump)))) 
    #int형으로 바뀌면서 자동으로 011-> 11로 바뀌기 때문에 다시 한 번 중복 제거 해줘야 함


    for i in nump:
        if i != 0 and i != 1:
            so = 0
            for k in range(2,i):
                if i%k == 0:
                    so = 1
                    break #소수 아님으로 판정 되면 바로 break를 해줘야 시간초과 안난다
            if so == 0:
                answer +=1
                        
    return answer