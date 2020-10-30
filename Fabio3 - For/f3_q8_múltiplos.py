z = 'Múltiplos'
print(f'{z:=^30}')
#01
n = int(input('Digite um número inteiro:\n>>> '))
l_i = int(input('Limite Inferior:\n>>> '))
l_s = int(input('Limite Superior:\n>>> '))
#02
for i in range(l_i, l_s+1):
    if l_i % n == 0:
        print(l_i)
    l_i += 1
