N = int(input())
arr_N = input()
arr_N = list(map(int, arr_N.split()))

for i in range(N):
  if i == 0:
    max = min = arr_N[i]
  if arr_N[i] > max:
    max = arr_N[i]
  if arr_N[i] < min:
    min = arr_N[i]

print(min, max)