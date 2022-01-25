# 백준 13022 늑대와 올바른 단어

import sys
input = sys.stdin.readline


def check(seq, dic):
    if ''.join(seq) == 'wolf' and dic['w'] == dic['o'] == dic['l'] == dic['f']:
        seq = []
        dic = dict(w=0, o=0, l=0, f=0)
        pass
    else:
        print(0)
        sys.exit(0)
    return seq, dic


word = list(input().rstrip())
if len(word) < 4:
    print(0)
    sys.exit(0)

# wolf 순서 체크를 위한 seq
former = word[0]
seq = [former]

# wolf 개수 체크를 위한 dic
dic = dict(w=0, o=0, l=0, f=0)
dic[former] = 1

for i in range(1, len(word)):
    if word[i] != former:
        if former == 'f':
            seq, dic = check(seq, dic)
        seq.append(word[i])
        former = word[i]

    dic[word[i]] += 1

    if i == len(word) - 1:
        seq, dic = check(seq, dic)

print(1)
