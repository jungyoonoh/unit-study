# 5800번 성적 통계 (Implementation) 
# https://www.acmicpc.net/problem/5800

N = int(input())

for i in range(N):
    info = list(map(int, input().split()))
    print("Class", i+1)
    res = sorted(info[1:], reverse=True)
    large = 0
    for i in range(len(res) - 1):
        large = max(large, res[i] - res[i+1])
    s = "Max " + str(max(res)) + ", Min " + str(min(res)) + ", Largest gap " + str(large)
    print(s)