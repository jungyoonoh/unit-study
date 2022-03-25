# 프로그래머스 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

def reverseBrackets(p):
    temp = ''
    for i in range(len(p)):
        if p[i] == '(':
            temp += ')'
        else:
            temp += '('
    return temp
    
def checkCorrect(p):
    stack = []
    stack.append(p[0])
    for i in range(1, len(p)):
        if p[i] == ')' and stack[-1] == '(':
            stack.pop()
            continue
        stack.append(p[i])
                        
    return len(stack) == 0

def dfs(p):
    if len(p) == 0:
        return ''
    
    left, right, idx = 0, 0, -1
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            idx = i + 1
            break
    
    u, v = p[:idx], p[idx:]
    
    if checkCorrect(u):
        return u + dfs(v)
    else:
        return '(' + dfs(v) + ')' + reverseBrackets(u[1:len(u)-1])

def solution(p):        
    return dfs(p)