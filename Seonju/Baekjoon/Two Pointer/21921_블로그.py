# 백준 21921 블로그

import sys
input = sys.stdin.readline

# 블로그를 시작하고 지난 일수 n
# x일 동안 가장 많이 들어온 방문자 수를 출력
n, x = map(int, input().split())
people = list(map(int, input().split()))

maximum = 0
end = 0
summary = 0
cnt = 0 # 방문자수 제일 많았던 기간이 몇 개인지
for start in range(n):
    while summary <= maximum and end < start + x and end < n:
        summary += people[end]
        if summary > maximum:
            maximum = summary
            cnt = 1
        elif summary == maximum:
            cnt += 1
        end += 1
    summary -= people[start]

if maximum == 0:
    print("SAD")
else:
    print(maximum, cnt, sep='\n')
