z = 'Prefeitura'
print(f'{z:=^30}')
#01
def Prefeitura():
    n = int(input('Digite o número de habitantes:\n>>> '))
    print('='*30)
    
    for i in range(0, n, 1):
        print(f'*** Ficha {i+1} *** ')
        salário = float(input('Salário:\n>>> '))
        número_filhos = int(input('Número de filhos:\n>>> '))

        
Prefeitura()