z = 'Múltiplos'
print(f'{z:=^30}')
#01
n = int(input('Digite um número inteiro:\n>>> '))
l_i = int(input('Limite Inferior:\n>>> '))
l_s = int(input('Limite Superior:\n>>> '))
#02
while l_i <= l_s:
    if l_i % n == 0:
        print(l_i)
    l_i += 1
