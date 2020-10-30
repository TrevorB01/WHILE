z = 'Maior Quadrado Menor ou Igual'
print(f'{z:=^35}')
#01
def main():
    valor_maximo = int(input('Digite um número inteiro:\n>>> '))
    num = 1

    for i in range(num ** 2, valor_maximo+1):
        quadrado = num ** 2
        num += 1

    print(quadrado) 
    

main()
