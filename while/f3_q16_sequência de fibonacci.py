z = 'Sequência de Fibonacci'
print(f'{z:=^30}')
#01
def main():
    quant = int(input('Digite um número inteiro:\n>>> '))

    quant_atual = 2
    anterior = 0
    atual = 1

    print(anterior, atual, end=' ')

    while quant_atual < quant:
        novo_atual = anterior + atual
        anterior = atual
        atual = novo_atual

        print(atual, end=' ')
        quant_atual += 1

    print()

main()
