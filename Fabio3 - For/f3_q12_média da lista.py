z = 'Média da Lista'
print(f'{z:=^30}')
#01
def main():
    n = int(input('Digite um número inteiro:\n>>> '))
    a = 0
    m = n

    
    for i in range(n):
        a += n
        n -= 1

    med = a / m
    
    print(f'A soma é {a}')
    print(f'A média é {med}')

main()
