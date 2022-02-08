# 백준 1343 폴리오미노

board = input()
ans = board.replace('XXXX', 'AAAA').replace('XX', 'BB')

if ans.count('X') > 0:
    print(-1)
else:
    print(ans)