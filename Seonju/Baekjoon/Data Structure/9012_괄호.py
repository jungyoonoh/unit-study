# 백준 9012 괄호

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    stack = []
    ps = list(input().rstrip())
    while ps:
        if ps[0] == '(':
            stack.append(ps[0])
        elif ps[0] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ps[0])
        del ps[0]

    if len(stack):
        print('NO')
    else:
        print('YES')
