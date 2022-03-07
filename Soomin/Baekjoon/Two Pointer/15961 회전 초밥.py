#20220305
#백준(투포인터) : 15961 회전 초밥#https://www.acmicpc.net/problem/15961

n, d, k, c = map(int, input().split())
sushi = []

for _ in range(n):
  sushi.append(int(input()))
sushi += sushi[:k-1] 


eat = [0] * (d+1)
eat[c] = 1 #쿠폰으로 먹음

ans = 1

for i in range(k):
  s = sushi[i]

  if eat[s] == 0:
    eat[s] += 1
    ans += 1
  else: # 이미 먹은 적 있는 숫자는 답에 영향X
    eat[s] += 1


start = 0
end = k
hap = ans

for i in range(end,len(sushi)):

  # 제일 앞 빼고
  eat[sushi[start]] -= 1
  
  # 2개 이상 있던 경우 제외
  if eat[sushi[start]] == 0:
    hap -= 1

  # 뒤에 하나 추가
  eat[sushi[i]] += 1
  if eat[sushi[i]] == 1:
    hap += 1
  
  ans = max(hap, ans)
  start +=1 #시작 위치 이동


print(ans)
  