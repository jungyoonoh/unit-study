# 20310번 타노스 (String) 
# https://www.acmicpc.net/problem/20310

S = list(input())
z, o = S.count('0') // 2, S.count('1') // 2

for _ in range(z):
    S.pop(-S[::-1].index('0') - 1)

for _ in range(o):
    S.pop(S.index('1'))

print(''.join(S))