z = 'Fazendeiro'
print(f'{z:=^30}')
#01
def Fazendeiro():
    n = int(input('Digite o número de fichas:\n>>> '))
    print('='*30)
    
    id_magro = -1
    id_gordo = -1
    peso_magro = -1
    peso_gordo = -1

    for i in range(n):
        print(f'*** Ficha {i+1} *** ')
        id = input('Indentificação:\n>>> ')
        nome = input('Nome:\n>>> ')
        peso = float(input('Peso(kg):\n>>> '))

        if i == 0:
            id_magro = id
            id_gordo = id
            peso_magro = peso
            peso_gordo = peso
        else:
            if peso < peso_magro:
                id_magro = id
                peso_magro = peso
            if peso > peso_gordo:
                id_gordo = id
                peso_gordo = peso
        print('='*30)
    print('*** Resultado ***')
    print(f'Boi mais magro:\nid = {id_magro}\npeso = {peso_magro}kg\n')
    print(f'Boi mais gordo:\nid = {id_gordo}\npeso = {peso_gordo}kg\n')

    
Fazendeiro()
