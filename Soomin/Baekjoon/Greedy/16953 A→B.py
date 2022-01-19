#20220119
#백준(그리디) : 16953 A→B
#https://www.acmicpc.net/problem/16953

a,b = map(int,input().split())
count = 1

while (b != a):
  # b 짝수 
  if b % 2 == 0: 
    b = b // 2
    count += 1

  # b 홀수
  elif b % 2 == 1:
    bb = list(str(b))
    # b 끝이 1이고, a보다 작지 않으면
    if bb[-1] == '1' and b >= a:
      b = int(''.join(bb[:-1])) #뒤에 1 제거해줌
      count += 1
    else: # 끝이 1이 아니거나 a보다 b가 작으면
      count = -1
      break

print(count)

