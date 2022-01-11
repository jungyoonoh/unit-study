# 백준 16165 걸그룹 마스터 준석이

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 걸그룹 수, m은 퀴즈 수
team = {}

for _ in range(n):
    name = input().rstrip() # 팀 이름 저장
    team[name] = []
    for _ in range(int(input())): # 멤버 이름 저장
        team[name].append(input().rstrip())
    team[name].sort()

for _ in range(m): # 1: 팀 출력, #0: 멤버 출력
    quiz = input().rstrip()
    num = int(input())
    if num == 1:
        print(''.join([key for key, value in team.items() if quiz in value]))
    else:
        print('\n'.join(*[value for key, value in team.items() if quiz in key]))