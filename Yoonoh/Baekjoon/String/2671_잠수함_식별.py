# 2671번 잠수함 식별 (String) 
# https://www.acmicpc.net/problem/2671

# (100~1~|01)~ : 잠수함 소리
# 10 하고 0을 계속 반복할 수 있으며, 그 뒤에 1이 하나 나와야하고 1을 계속 반복할 수 있다 또는 01 이라는 문자열을 찍는다.
# 위와 같은 패턴을 가진 문자열을 (()로 묶인단위) 계속 반복할 수 있음. 

import re

sound = input()
pattern = "(100+1+|01)+" 
c = re.compile(pattern)
print("SUBMARINE" if c.fullmatch(sound) else "NOISE")