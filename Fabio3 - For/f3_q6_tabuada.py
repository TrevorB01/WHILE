z = 'TABUADA'
print(f'{z:=^30}')
#01
t = int(input('Tabuada do: '))

num_fixo = t
valor_mult = 1


for i in range(10):
    reslt = valor_mult * num_fixo 
    print(valor_mult, 'x',reslt)
    
    valor_mult += 1
