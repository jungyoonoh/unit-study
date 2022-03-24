
while True:
  n = list(map(str,input()))
  n = list(map(int,n))

  if n[0] == 0:
    exit(0)
    
  a = n[:len(n)//2]
  b = n[::-1]
  b = b[:len(n)//2]  

  if a == b:
    print("yes")
  else:
    print("no")  