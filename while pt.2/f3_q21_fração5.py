z = 'Fração 5'
print(f'{z:=^30}')
#01
def Fração():
    n = int(input('Digite um número inteiro:\n>>> '))
    print('='*30)
    cont = 1
    um = 1

    while um <= n:
        print(cont, '/', um)
        um += 1
        cont += 2
        


Fração()