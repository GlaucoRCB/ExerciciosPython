frutas = ['maça', 'banana', 'maça', 'maça', 'mamao']
contar_fruta = 0

for fruta in frutas:
    print(fruta)
    if(fruta == 'maça'):
        contar_fruta += 1

print(f'a palavra maça apareceu {contar_fruta} vezes')