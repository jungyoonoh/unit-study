# 15787번 기차가 어둠을 헤치고 은하수를 (Implementation) 
# https://www.acmicpc.net/problem/15787

# 1 i x = i번째 기차의 x번째 자리에 사람을 태우세요
# 2 i x = i번째 기차에 x번째 자리에 사람 내리게 하세요
# 3 i = i번째 기차에 앉은 사람들 하나씩 뒤로가세요
# 4 i = i번째 기차에 앉은 승객 모두 한칸씩 앞으로 가세요

N, M = map(int, input().split())

train = [['0' for _ in range(20)] for _ in range(N+1)]
for i in range(M):
    command = list(map(int, input().split()))
    
    if command[0] == 3:
        train[command[1]].insert(0, '0')
        train[command[1]].pop()
        continue

    if command[0] == 4:        
        train[command[1]].append('0')
        del train[command[1]][0]
        continue
    
    if command[0] == 1:
        train[command[1]][command[2] - 1] = '1'
        continue
    
    train[command[1]][command[2] - 1] = '0'

canCrossGalaxy = set()
cnt = 0
for i in range(1, N+1):
    s = ''.join(train[i])
    if s in canCrossGalaxy:
        continue
    
    canCrossGalaxy.add(s)
    cnt += 1

print(cnt)