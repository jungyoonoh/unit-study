# 프로그래머스 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 양궁대회
# https://programmers.co.kr/learn/courses/30/lessons/92342

import itertools

scoreBoardSize = 11
def determineWinner(apeachShot, lionShot):
    # 승자, 점수차
    apeachScore = lionScore = 0
    for i in range(scoreBoardSize):
        if apeachShot[i] < lionShot[i]:
            if lionShot[i] != 0:
                lionScore += 10 - i
        else:
            if apeachShot[i] != 0:
                apeachScore += 10 - i
    
    winner = ('apeach' if apeachScore >= lionScore else 'lion')
    gap = abs(lionScore - apeachScore)
    
    return (winner, gap)

def checkLessScoreShot(recordedScoreBoard, nowScoreBoard):
    for i in range(10, -1, -1):
        if recordedScoreBoard[i] < nowScoreBoard[i]:
            return nowScoreBoard
        elif recordedScoreBoard[i] > nowScoreBoard[i]:
            return recordedScoreBoard
        
    return [-1]

def solution(n, info):
    totalCase = list(itertools.combinations_with_replacement([i for i in range(scoreBoardSize)], n))
    lionShotInfo = [0] * scoreBoardSize 
    scoreGap = -1
    for case in totalCase:
        caseOfLion = [0] * scoreBoardSize
            
        for i in case:
            caseOfLion[i] += 1
            
        winner, gap = determineWinner(info, caseOfLion)
        if winner == 'lion':
            if scoreGap < gap: 
                scoreGap = gap
                for i in range(scoreBoardSize):
                    lionShotInfo[i] = caseOfLion[i]
            elif scoreGap == gap: # 아랫 점수를 더 많이 맞춰서 이기는 경우 캐치
                lionShotInfo = checkLessScoreShot(lionShotInfo, caseOfLion)
                    
    if scoreGap == -1:
        lionShotInfo = [-1]
        
    return lionShotInfo