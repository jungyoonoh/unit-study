# 프로그래머스 코딩테스트 연습 > 탐욕법 > 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    loss = set(lost)
    rest = set(reserve) 
    intersecs = rest & loss
    rest = rest - intersecs
    loss = loss - intersecs
    answer = n - len(loss)
    cnt = 0
    for n in loss:
        if n-1 in rest:
            rest.remove(n-1)
            cnt += 1
            continue
        elif n+1 in rest:
            rest.remove(n+1)
            cnt += 1
            continue

    return answer + cnt

print(solution(5,[1, 2, 4],[1, 3, 5]))