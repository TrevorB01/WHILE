z = 'Fatorial'
f = 'FOR'
print(f'{f:=^30}')
print(f'{z:=^30}')
#01
def fatorial():
    n = int(input('Digite um número:\n>>> '))
    f = 1

    for i in range(n):
        f *= n
        n -= 1
    print(f'O fatorial é {f}')


fatorial()

