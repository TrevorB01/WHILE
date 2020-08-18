z = 'Maior Quadrado Menor ou Igual'
print(f'{z:=^35}')
#01
def main():
    n = int(input('Digite um número inteiro:\n>>> '))
    num = 1

    while num ** 2 <= n:
        quadrado = num ** 2
        num += 1

    print(quadrado) 
    

main()
