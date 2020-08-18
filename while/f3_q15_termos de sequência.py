z = 'Termos de Sequência'
print(f'{z:=^30}')
#01
def main():
    n = int(input('Inserir número, para gerar a sequência de Fibonnaci:\n>>> '))

    u_1 = 1
    u_2 = 1


    lista = [u_1,u_2]

    for vic in range(0, n):
        c = u_1 + u_2
        u_1 = c
        u_2 = (c - u_2)
        lista.append(c)

    print(lista)


main()