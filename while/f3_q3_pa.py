z = 'P.A.'
print(f'{z:=^30}')
#01
a = int(input('Número inicial:\n>>> '))
limite = int(input('Número final:\n>>> '))
r = int(input('Razão:\n>>> '))
#02
while a < limite:
    print(a)
    a += r
