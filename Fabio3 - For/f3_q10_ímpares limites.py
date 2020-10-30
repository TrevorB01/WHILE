z = 'Ímpares Limites'
print(f'{z:=^30}')
#01
def main():
    l_i = int(input('Limite Inferior:\n>>> '))
    l_s = int(input('Limite Superior:\n>>> '))

    for i in range(l_i , l_s):
        if l_i % 2 == 1:
            print(l_i)
        l_i += 1

main()
