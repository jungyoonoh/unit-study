# 1049번 기타줄 (Greedy) 
# https://www.acmicpc.net/problem/1049

N, M = map(int, input().split())
package = []
each = []
for i in range(M):
    p, e = map(int, input().split())
    package.append(p)
    each.append(e)

package.sort()
each.sort()

if package[0] >= each[0] * 6:
    print(each[0] * N)
else:
    price = (N // 6) * package[0] 
    price += package[0] if (each[0] * (N % 6)) > package[0] else (each[0] * (N % 6))
    print(price)