z = 'P.A.'
f = 'FOR'
print(f'{f:=^30}')
print(f'{z:=^30}')
#01
def pa():
    a = int(input('Número inicial:\n>>> '))
    limite = int(input('Número final:\n>>> '))
    r = int(input('Razão:\n>>> '))

    for i in range(a, limite+1, r):
        print(a)
        a += r


pa()