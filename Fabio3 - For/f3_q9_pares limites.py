z = 'Pares Limites'
print(f'{z:=^30}')
#01
l_i = int(input('Limite Inferior:\n>>> '))
l_s = int(input('Limite Superior:\n>>> '))
#02
for i in range(l_i , l_s):
    if l_i % 2 == 0:
        print(l_i)
    l_i += 1
