# 9466번 텀 프로젝트 (DFS) 
# https://www.acmicpc.net/problem/9466

TC = int(input())
for i in range(TC):
    n = int(input())
    student = [0] + list(map(int, input().split()))
    team = [0] * (n+1)
    for i in range(1, n+1):        
        if team[i] == 0:
            teamNum = i # parent 지정
            
            #1. 본인선택 : 다음 team[i] val이 teamNum
            #2. cycle 발견 : i = cycle start를 가리킴
            #3. cycle 안됨 : team[i] val이 (parent)인 채로 종료
            while team[i] == 0:                                
                team[i] = teamNum
                i = student[i]
            
            while team[i] == teamNum:
                team[i] = -1
                i = student[i]
            
    res = n - team.count(-1)
    print(res)