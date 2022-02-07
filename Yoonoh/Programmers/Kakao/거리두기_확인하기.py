# 프로그래머스 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302

d1YVec = [-1, 0, 1, 0] # 12 3 6 9
d1XVec = [0, 1, 0, -1]
d2YVec = [-2, -1, 0, 1, 2, 1, 0, -1] # 12 1 3 5 6 7 9 11
d2XVec = [0, 1, 2, 1, 0, -1, -2, -1] 

def checkSocialDistancing(places):
    N = len(places)
    print(places)
    for i in range(N):
        for j in range(N):
            if places[i][j] == 'P':
                y, x = i, j 
                for k in range(4):
                    ny = y + d1YVec[k]
                    nx = x + d1XVec[k]
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue
                    
                    if places[ny][nx] == 'P':
                        return 0
                
                for k in range(8):
                    ny = y + d2YVec[k]
                    nx = x + d2XVec[k]
                    
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue
                    
                    if places[ny][nx] == 'P':                    
                        # 직선
                        if (d2YVec[k] == 0 or d2XVec[k] == 0):
                            if places[y + d2YVec[k] // 2][x + d2XVec[k] // 2] != 'X':
                                return 0
                            else: 
                                continue             
                        if places[ny][x] != 'X' or places[y][nx] != 'X':
                            return 0
                            
    return 1

def solution(places):
    answer = []
    for i in range(len(places)):
        answer.append(checkSocialDistancing(places[i]))
    return answer