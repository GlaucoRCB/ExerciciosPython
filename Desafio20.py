# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1,101))

for numero in numeros:
    if(numero % 2 == 0):
        print(f'o número {numero} é par')
    else:
        print(f'o número {numero} é impar')