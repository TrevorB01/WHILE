z = 'TABUADA'
print(f'{z:=^30}')
#01
t = int(input('Tabuada do: '))

num_fixo = t
valor_mult = 1

while valor_mult <= 10:
    reslt = valor_mult * num_fixo
    print(reslt)

    valor_mult += 1
