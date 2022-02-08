# 프로그래머스 거리두기 확인하기 (2021 카카오 채용연계형 인턴십)

from itertools import combinations


def solution(places):
    answer = []

    for num in range(5):  # num: 대기실 인덱스

        pos = []  # pos: P의 위치를 담을 리스트
        for i in range(5):
            for j in range(5):
                if places[num][i][j] == 'P':
                    pos.append((i, j))

        is_correct = 1  # is_correct: 거리두기가 지켜졌는지를 나타내는 boolean 값
        com = list(combinations(pos, 2))  # com: 두 개의 P 위치를 조합해 묶어놓은 리스트

        for i in range(len(com)):
            x1 = com[i][0][0]
            x2 = com[i][1][0]
            y1 = com[i][0][1]
            y2 = com[i][1][1]
            dist = abs(x1 - x2) + abs(y1 - y2)

            # 두 P 사이 거리가 2 이하라면 중간에 파티션이 있는지 검사
            if dist <= 2:
                # 가로 검사
                if x1 == x2 and places[num][x1][max(y1, y2) - 1] == 'X':
                    continue
                # 세로 검사
                elif y1 == y2 and places[num][max(x1, x2) - 1][y1] == 'X':
                    continue
                # 대각선 검사
                elif abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
                    if places[num][x1][y2] == 'X' and places[num][x2][y1] == 'X':
                        continue
                # 아무데서도 파티션을 발견하지 못했다면 거리두기 실패
                is_correct = 0
                break

        answer.append(is_correct)

    return answer
