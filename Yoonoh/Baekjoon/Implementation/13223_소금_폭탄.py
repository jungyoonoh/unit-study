# 13223번 소금 폭탄 (Implementation) 
# https://www.acmicpc.net/problem/13223

nowH, nowM, nowS = map(int, input().split(":"))
saltH, saltM, saltS = map(int, input().split(":"))

nowTotal = nowH * 3600 + nowM * 60 + nowS
saltTotal = saltH * 3600 + saltM * 60 + saltS

if nowTotal >= saltTotal:
    saltTotal += 24 * 3600

gap = saltTotal - nowTotal

resS = gap % 60
resM = (gap // 60) % 60
resH = (gap // 3600)

resS, resM, resH = str(resS), str(resM), str(resH)
resS = "0" + resS if len(resS) == 1 else resS
resM = "0" + resM if len(resM) == 1 else resM
resH = "0" + resH if len(resH) == 1 else resH

print(resH + ":" + resM + ":" + resS)