z = 'P.G.'
print(f"{z:=^30}")
#01
a = int(input('Número inicial:\n>>> '))
limite = int(input('Número final:\n>>> '))
r = int(input('Razão:\n>>>> '))
#02
while a < limite:
    a *= r
    print(a)
