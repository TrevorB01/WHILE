z = 'Empresa'
print(f'{z:=^30}')
#01
def Empresa():
    n = int(input('Digite o número de funcionário:\n>>> '))
    print('='*30)
    
    for i in range(0, n, 1):
        print(f'*** Ficha {i+1} *** ')
        codigo = int(input('Código:\n>>> '))
        hrs_trabalho = float(input('Número de horas trabalhadas:\n>>> '))
        depententes = int(input('Número de dependentes:\n>>> '))
        
        valor_hr = hrs_trabalho * 12
        valor_deprendente = depententes * 40

        salario_b =  valor_hr + valor_deprendente

        inss = salario_b * 0.085
        ir = salario_b * 0.05

        desconto = inss + ir

        salario_l = salario_b - desconto
        print('='*30)

        print(f'Salário bruto: {salario_b:.2f}\n')
        print(f'INSS: {inss:.2f}\nIR: {ir:.2f}\n') 
        print(f'Salário líquido: {salario_l:.2f}')

        
        print('='*30)

    
Empresa()
