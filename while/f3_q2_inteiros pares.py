z = 'Inteiros Pares'
print(f'{z:=^30}')
#01
n = 1
num = int(input('Digete um número inteiro:\n>>> '))
#02
while n <= num:
    if n % 2 == 0:
        print(f'{n}')
    n += 1
