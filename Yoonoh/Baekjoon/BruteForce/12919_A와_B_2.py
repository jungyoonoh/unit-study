# 12919번 A와 B 2 (BruteForce) 
# https://www.acmicpc.net/problem/12919

# A___A -> 1번 방법만 가능
# B___A -> 1,2번 방법 둘 다 가능
# 왜냐하면 1번 방법으로 맨 뒤에 있는 A를 없앨 수 있고,
# 2번 방법으로 문자열을 먼저 뒤집고 맨 뒤의 B를 없앨 수 있기 때문이다.
# A___B -> 1,2번 둘다 X
# B___B -> 2번 방법만 가능
# 따라서 T[-1] == 'A' or T[0] == 'B' 인 경우만 고려한다

# 처음에는 분기에 따라 복사해서 값을 넘겨서 메모리 초과가 발생했다.

from collections import deque

S = list(input())
T = list(input())
dq = deque(S)
limit = len(T)

def findStr(s, t):
    if len(s) == len(t):
        return s == t       
    
    if len(s) > len(t):
        print(0)
        return False
    
    if t[-1] == 'A' and findStr(s, t[:-1]) == 1:
        return 1
    
    if t[0] == 'B' and findStr(s, t[::-1][:-1]) == 1:
        return 1
    
    return 0

print(findStr(S, T))
