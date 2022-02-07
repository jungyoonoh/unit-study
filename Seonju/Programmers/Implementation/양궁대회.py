# 프로그래머스 양궁대회 (2022 KAKAO BLIND RECRUITMENT)

from collections import deque


def bfs(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])

    while q:
        focus, arrow = q.popleft()
        if sum(arrow) == n:  # 화살 다 쏜 경우
            apeach = 0
            lion = 0
            for i in range(11):
                if info[i] != 0 or arrow[i] != 0:
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                res.append((lion - apeach, arrow))  # 라이언이 이기는 경우는 (점수차, 라이언 화살상황) 형태로 전부 res에 추가
        elif sum(arrow) > n:  # 화살 더 쏜 경우 제외
            continue
        elif focus == 10:  # 화살 덜 쏜 경우 남은 화살 다 0점에 쏴주기
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1  # 어피치보다 1발 많이 쏘기
            q.append((focus + 1, tmp))
            tmp2 = arrow.copy()
            tmp2[focus] = 0  # 0발 쏘기
            q.append((focus + 1, tmp2))

    return res


def solution(n, info):
    lst = bfs(n, info)

    if len(lst) == 0:  # 라이언이 이기는 경우가 없을 때
        answer = [-1]

    else:  # 라이언이 이기는 경우가 있을 때
        mx = max(lst)[0]  # 가장 큰 점수차 구하기
        compare = []
        for i in lst:  # 가장 큰 점수차를 내는 화살상황 구하기
            if i[0] == mx:
                compare.append(i[1])

        if len(compare) == 1:  # 가장 큰 점수차를 내는 화살상황이 1개면 그대로 answer행
            answer = compare[0]
        else:  # 여러개면
            ans = []
            for i in range(len(compare)):  # 각각의 화살상황에 대해
                for j in range(10, -1, -1):  # 화살상황 맨 뒤부터 체크하면서
                    if compare[i][j] != 0:  # 값이 0이 아닐 때를 찾음
                        ans.append([i, j, compare[i][j]])
                        break
            ans.sort(key=lambda x: (-x[1], x[2]))  # 가장 낮은 점수순, 그걸 맞춘 횟수순으로 정렬
            answer = compare[ans[0][0]]  # 정답 도출

    return answer
