z = 'Fração 1'
print(f'{z:=^30}')
#01
def Fração():
    n = int(input('Digite um número inteiro:\n>>> '))
    print('='*30)
    cont = 1
    um = 1

    while cont <= n:
        print(um, '/', cont, '=', f'{um / cont:.2f}',)
        cont += 1


Fração()