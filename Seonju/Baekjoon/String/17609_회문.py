# 백준 17609 회문

import sys
input = sys.stdin.readline


def check_palin(word, flag):
    # flag는 한 문자를 삭제할 수 있는 상황인지를 나타냄
    start, end = 0, len(word) - 1
    is_palin = 1

    while start < end:
        if word[start] != word[end] and not flag:
            is_palin = 0
            break
        elif word[start] != word[end] and flag:
            if check_palin(word[start+1:end+1], 0)[0]:  # start 쪽에서 한 문자 삭제
                flag = 0
                start += 1
            elif check_palin(word[start:end], 0)[0]:  # end 쪽에서 한 문자 삭제
                flag = 0
                end -= 1
            else:
                is_palin = 0
                break
        start += 1
        end -= 1

    return is_palin, flag


for _ in range(int(input())):
    string = input().rstrip()
    is_palin, flag = check_palin(string, 1)

    if is_palin and flag:
        print(0)
    elif is_palin and not flag:
        print(1)
    else:
        print(2)