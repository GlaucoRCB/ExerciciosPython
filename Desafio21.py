cidades = ('São Paulo', 'Rio de Janeiro', 'Recife')
pesquisa_cidade = input('Digite o nome de uma cidade: ')

if pesquisa_cidade in cidades:
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')