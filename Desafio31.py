par_impar = lambda x: 'par' if (x % 2 == 0)  else 'impar'
numero = int(input('Digite um número: '))
print(f'O número {numero} é {(par_impar(numero))}')