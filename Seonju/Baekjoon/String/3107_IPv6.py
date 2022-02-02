# 백준 3107 IPv6

adr = list(input().split(':'))

if adr.count(''):
    while len(adr) > 8:
        del adr[adr.index('')]
    while len(adr) < 8:
        adr.insert(adr.index(''), '0000')

for i in range(len(adr)):
    if len(adr[i]) < 4:
        adr[i] = '0'*(4-len(adr[i])) + adr[i]

print(*adr, sep=':')