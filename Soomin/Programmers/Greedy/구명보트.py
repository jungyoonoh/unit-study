#20220202
#프로그래머스(그리디) : 구명보트
#https://programmers.co.kr/learn/courses/30/lessons/42885

#효율성 테스트 통과 못함

def solution(people, limit):
    people.sort(reverse = True)
    b = [[limit,0]]

    for i in range(len(people)):
        last = 0
        for j in range(len(b)):
            if b[j][0] >= people[i] and b[j][1] < 2:
                b[j][0] -= people[i]
                b[j][1] += 1
                last = 1
                break
                           
        if last == 0:
             b.append([limit-people[i],1])
    
    
    answer = len(b)
    return answer