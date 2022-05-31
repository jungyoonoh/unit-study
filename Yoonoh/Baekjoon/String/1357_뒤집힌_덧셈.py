# 1357번 뒤집힌 덧셈 (String) 
# https://www.acmicpc.net/problem/1357

x, y = map(int, input().split())

def rev(n):
    if n < 10:
        return n
    reverse = []
    while n:
        reverse.append(str(n % 10))
        n = n // 10
    return int(''.join(reverse))

print(rev(rev(x) + rev(y)))