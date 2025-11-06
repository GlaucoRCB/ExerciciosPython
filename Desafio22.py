pais_capital = {
    "Brasil": 'Brasília',
    "Argentina": 'Buenos Aires',
    "França": 'Paris',
    "Japão": 'Tóquio',
    "Canadá": 'Ottwa'
}

pesquisa_pais = input('Digite o nome de um pais: ')

if pesquisa_pais in pais_capital:
    print(f'A capital do pais {pesquisa_pais} é {pais_capital['Brasil']}')
else:
    print('Desculpe não temos informações sobre a capital desse país')