carros = ['BMW X6', 'BMW I5', 'BMWI8']
carro_desejado = input('Qual carro deseja: ')

if carro_desejado in carros:
    print("Este carro está disponível!")
else:
    print("Desculpe, este carro não está disponível.")