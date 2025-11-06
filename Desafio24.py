# minha solução
'''def quadrado_numero():
    numero = float(input('Digite um número: '))
    numero_quadrado = numero ** 2
    print(f'O quadrado de {numero} é {numero_quadrado}')

quadrado_numero()'''

# solução melhorada
def quadrado(numero):
    return numero ** 2

num = float(input('Digite um número: '))
print(f'O quadrado de {num} é {quadrado(num)}')