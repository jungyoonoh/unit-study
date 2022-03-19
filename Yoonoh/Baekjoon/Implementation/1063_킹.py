# 1063번 킹 (Implementation) 
# https://www.acmicpc.net/problem/1063

# 오 왼 아 위 오위 왼위 오아 왼아
dy = [0, 0, -1, 1, 1, 1, -1, -1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dir = {'R':0, 'L':1, 'B':2, 'T':3, 'RT':4, 'LT':5, 'RB':6, 'LB':7}

king, stone, N = map(str, input().split())
ky, kx = int(king[1]) - 1, ord(king[0]) - ord('A')
sy, sx = int(stone[1]) - 1, ord(stone[0]) - ord('A')

for i in range(int(N)):
    command = dir[input().strip()]
    nky, nkx = ky + dy[command], kx + dx[command]
    
    if nky < 0 or nkx < 0 or nky >= 8 or nkx >= 8:
        continue
    
    if nky == sy and nkx == sx:
        nsy, nsx = sy + dy[command], sx + dx[command]
        
        if nsy < 0 or nsx < 0 or nsy >= 8 or nsx >= 8:
            continue
        
        sy, sx = nsy, nsx
    
    ky, kx = nky, nkx

ky, kx = str(ky + 1), chr(kx + ord('A'))
sy, sx = str(sy + 1), chr(sx + ord('A')) 
print(kx+ky)
print(sx+sy)