#20220406
#백준(문자열) : 1972 놀라운 문자열
#https://www.acmicpc.net/problem/1972

while True:
  s = input()
  if s=="*":
    break

  for i in range(1,len(s)-1):
    ss = set()
    for j in range(len(s)-i):
      surprise = s[j] + s[i+j]

      if surprise in ss:
        print(s, "is NOT surprising.")
        break

      else:
        ss.add(surprise)
    else:
      continue
    break
  else:
    print(s,"is surprising.")
        
        