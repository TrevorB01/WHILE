z = 'Fração 4'
print(f'{z:=^30}')
#01
def Fração():
    n = int(input('Digite um número inteiro:\n>>> '))
    print('='*30)
    cont = 1
    um = 1

    while cont <= n:
        if cont % 2 == 1:
            print(um, '/', cont)
        else:
            print('-', um, '/', cont)
        cont += 1


Fração()