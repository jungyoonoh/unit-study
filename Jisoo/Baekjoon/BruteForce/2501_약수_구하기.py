arr = input()
arr = arr.split(" ")

n = int(arr[0])
k = int(arr[1])

yak_n = []

for i in range(1, n + 1):
    if (n % i == 0):
        yak_n.append(i)

if len(yak_n) < k:
    print('0')
else:
    print(yak_n[k - 1])