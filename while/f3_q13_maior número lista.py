z = 'Maior Número da Lista.'
print(f'{z:=^30}')
#01
def main():
    n = int(input('Digite um número inteiro:\n>>> '))
    c = 1
    m = n

    while c <= n:
        print(c)
        c += 1
    print('='*30)
    print(f'O maior Número é {m}')

main()
