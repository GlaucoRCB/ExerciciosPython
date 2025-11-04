frutas = ['maça', 'banana', 'manga', 'uva']

#trocar algo dentro da lista
frutas[1] = 'morango'
#adicionar algo no fim da lista
frutas.append('abacaxi')
print(frutas)


#trocar do index 1 até o 3 mas não incluindo o 3 index
frutas[1:3] = ['acabaxi', 'abacate']
#inserir onde quiser
frutas.insert(2, 'abobora')
print(frutas)