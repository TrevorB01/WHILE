z = 'Fração 2'
print(f'{z:=^30}')
#01
def Fração():
    n = int(input('Digite um número inteiro:\n>>> '))
    print('='*30)
    cont = 1 
    um = 1

    while cont <= n:
        print(um, '/', n)
        um += 1
        n -= 1
        

Fração()