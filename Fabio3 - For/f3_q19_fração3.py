z = 'Fração 3'
print(f'{z:=^30}')
#01
def Fração():
    n = int(input('Digite um número inteiro:\n>>> '))
    print('='*30)
    cont = 1
    um = 1

    for i in range(cont, n+1):
        if um % 2 == 1:
            print(um, '/', n)
        else:
            print('-', n, '/', um)
        um += 1
        n -= 1


Fração()