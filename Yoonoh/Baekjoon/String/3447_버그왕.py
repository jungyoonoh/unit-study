# 3447번 버그왕 (String) 
# https://www.acmicpc.net/problem/3447

import sys
import re
source = sys.stdin.readlines()

for line in source:    
    while True:    
        res = re.sub("BUG", "", line)
        if 'BUG' not in res:
            print(res, end="")
            break
        else:
            line = res