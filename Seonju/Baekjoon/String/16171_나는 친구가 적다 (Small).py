# 백준 16171 나는 친구가 적다 (Small)

s = input()
k = input()

ans = ''

for i in s:
    if i not in '1234567890':
        ans += i

print(1 if k in ans else 0)