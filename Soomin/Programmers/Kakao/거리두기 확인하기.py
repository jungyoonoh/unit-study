#20220202
#프로그래머스(2021 카카오 채용연계형 인턴십) : 거리두기 확인하기
#https://programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []  
    for i in places:
        # 방 하나 - 자리 한 자리씩 리스트에 나누어 넣음 
        room = list(map(list,i)) 
        # 	[['P', 'O', 'O', 'O', 'P'], ['O', 'X', 'X', 'O', 'X'], ['O', 'P', 'X', 'P', 'X'], ['O', 'O', 'X', 'O', 'X'], ['P', 'O', 'X', 'X', 'P']]
        
        p = [] # 사람이 앉아 있는 곳
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    p.append((i,j))
        #[(0, 0), (0, 4), (2, 1), (2, 3), (4, 0), (4, 4)]
        
        
        m = [] #맨해튼 거리가 지켜지지 않은 자리 위치
        
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if abs(p[i][0]-p[j][0]) + abs(p[i][1]-p[j][1]) <= 2:
                    m.append([p[i],p[j]])
        # [[(2, 1), (2, 3)]]
        
        okk = [] # 한 방 / 모든 줄 체크
        
        # m 중에서 파티션 있는 경우 확인
        for i in m:
            ok = 0
            min1 = min(i[0][0],i[1][0]) # 2
            max1 = max(i[0][0],i[1][0]) # 2
            min2 = min(i[0][1],i[1][1]) # 1
            max2 = max(i[0][1],i[1][1]) # 3
            
            # min과 max 사이에 파티션이 있는지 탐색
            for p in range(min1,max1+1):
                    for q in range(min2,max2+1):
                        if room[p][q] == 'X':
                            ok = 1
                            # 대각선인 경우는
                            # O P P O 
                            # P X X P 인 경우도 체크해야 함
                            if (i[1][0] - i[0][0] == 1 and i[1][1] - i[0][1] == 1) or (i[1][0] - i[0][0] == 1 and i[0][1] - i[1][1] == 1):
                                if i[0][1] > i[1][1]:
                                    # 대각선 양쪽에 다 파티션 있는지 확인
                                    if room[i[0][0]][i[0][1]-1] == 'X' and room[i[1][0]][i[1][1]+1] == 'X': 
                                        ok = 1
                        
                                    else:
                                        ok = 0  
                                else:
                                    if room[i[0][0]][i[0][1]+1] == 'X' and room[i[1][0]][i[1][1]-1] == 'X':
                                        ok = 1
                                        
                                    else:
                                        ok = 0
                            break
                            
        
            if ok == 0:
                okk.append(0)

            else:
                okk.append(1)

        
        if 0 in okk: # 한 줄이라도 0이 있으면
            answer.append(0)
        else: 
            answer.append(1)

    return answer