# 백준 2744 대소문자 바꾸기

ans = ''

for i in input():
    if i.isupper():
        ans += i.lower()
    else:
        ans += i.upper()

print(ans)