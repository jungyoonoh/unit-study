# 백준 17413 단어 뒤집기 2

import sys
input = sys.stdin.readline

word = input().rstrip()
sub_word = ''
ans = ''
is_gual = 0

for i in range(len(word)):
    if word[i] == '<':  # 괄호가 오면
        if sub_word:
            ans += sub_word[::-1]
            sub_word = ''
        is_gual = 1
        ans += word[i]

    elif is_gual:  # 괄호가 시작된 상태면
        if word[i] == '>':
            is_gual = 0
        ans += word[i]

    elif word[i] == ' ':  # 공백이 오면 정답에 sub_word[::-1]+공백 추가
        ans += sub_word[::-1] + ' '
        sub_word = ''

    else:  # 공백이 아니면 sub_word에 차곡차곡 쌓기
        sub_word += word[i]
        if i == len(word) - 1:  # 입력이 끝나면 정답에 sub_word[::-1] 추가
            ans += sub_word[::-1]

print(ans)