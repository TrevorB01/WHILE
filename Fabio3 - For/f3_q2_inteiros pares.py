z = 'Inteiros Pares'
f = 'FOR'
print(f'{f:=^30}')
print(f'{z:=^30}')
#01
def num_pares():
    n = 1
    num = int(input('Digete um número inteiro:\n>>> '))

    for i in range(num):
        if n % 2 == 0:
            print(f'{n}')
        n += 1


num_pares()