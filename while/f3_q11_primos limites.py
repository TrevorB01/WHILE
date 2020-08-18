z = 'Primos Limites'
print(f'{z:=^30}')
#01
def main():
    l_i = int(input('Limite Inferior:\n>>> '))
    l_s = int(input('Limite Superior:\n>>> '))

    while l_i < l_s:
        if primo(l_i) == True:
            print(l_i)
        l_i += 1

def primo(num):
    a = 1
    c = 0
    while a <= num:
        if num % a == 0:
            c += 1
        a += 1
    if c > 2:
        return False
    else:
        return True


main()
