# 2460

nae = 0
than = 0
chong = [0]*11

for i in range(1, 11):
    x = input()
    x = x.split()
    x = list(map(int, x))
    nae = x[0]
    than = x[1]
    chong[i] = chong[i-1] - nae + than

max = chong[0]
for m in range(1, 11):
    if chong[m] > max:
        max = chong[m]

print(max)