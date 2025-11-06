def potencia(base, exp=2):
    return base ** exp

usuario_base = int(input('Digite o valor base: '))
usuario_exp = input('Digite o valor exp: ')
if usuario_exp:
    print(f'A potência do {usuario_base} elevado a {int(usuario_exp)} é igual a {potencia(usuario_base,int(usuario_exp))}')
else:
    print(f'A potência do {usuario_base} elevado é igual a {potencia(usuario_base)}')