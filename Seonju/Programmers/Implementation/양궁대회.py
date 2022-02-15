# 프로그래머스 양궁대회 (2022 KAKAO BLIND RECRUITMENT)

from collections import deque

def bfs(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) == n:  # 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                res.append((lion - apeach, arrow))

        elif sum(arrow) > n:  # 화살 더 쏜 경우
            continue

        elif focus == 10:  # 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))

        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))  # 어피치보다 1점 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))  # 0점 쏘기

    return res

def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        answer = [-1]

    else:
        maxGap = max(winList)[0]
        maxWinList = []  # 최대점수차를 내는 라이언의 화살 상태를 담을 곳
        for i in winList:
            if i[0] == maxGap:
                maxWinList.append(i[1])

        if len(maxWinList) == 1:  # 최대점수차를 내는 화살 상태가 하나라면
            answer = maxWinList[0]
        else:  # 여러개라면
            answer = maxWinList[-1]

    return answer