z = 'Fatorial'
print(f'{z:=^30}')
#01
n = int(input('Digite um número:\n>>> '))
f = 1
#02
while n > 0:
    f *= n
    n -= 1
print(f'O fatorial é {f}')
