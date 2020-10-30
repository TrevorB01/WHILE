z = 'Soma Entre'
print(f'{z:=^30}')
#01
n = int(input('Digite um número inteiro:\n>>> '))
s = 0
#02
for i in range(n):
    s += n
    n -= 1
#03
print(f'A soma é {s}')
