z = 'Fração 5'
print(f'{z:=^30}')
#01
def Fração():
    n = int(input('Digite um número inteiro:\n>>> '))
    print('='*30)
    cont = 1
    um = 1

    for i in range(um, n+1):
        print(cont, '/', um)
        um += 1
        cont += 2
        


Fração()