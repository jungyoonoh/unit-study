# 백준 14405 피카츄

word = input()
rep = word.replace("pi", "00").replace("ka", "00").replace("chu", "000")
if rep.count("0") == len(word):
    print("YES")
else:
    print("NO")