def dobro(num):
    return num * 2

def quadrado(num):
    return num * num

numero = int(input('Digite um número: '))
print(f'O quadrado do dobro de {numero} é {quadrado(dobro(numero))}')