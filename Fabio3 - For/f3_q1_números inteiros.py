z = 'Números Inteiros'
f = 'FOR'
print(f'{f:=^30}')
print(f'{z:=^30}')
#01

def Num_inteiros():

    num = int(input('Digite um número inteiro:\n>>> '))

    for i in range(1, num+1, 1):
        print(i)


Num_inteiros()