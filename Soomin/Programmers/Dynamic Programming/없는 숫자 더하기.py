#20220328
#프로그래머스(디피) : 없는 숫자 더하기
#https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):

    dp = [i for i in range(10)]
    
    for i in numbers:
        dp[i] = 0
    
    answer = sum(dp)
        
    return answer