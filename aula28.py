# Exercicio
# Peca ao Usuario para digitar seu nome 
# peca ao user para digitar sua idade
# Se nome e idade forem digitados:
#     exiba
#         Seu nome e {nome}
#         seu nome invertido e {nome envertido}
#         Seu nome Contem (ou nao) espacos
#         Seu nome tem {n} letras
#         A primeira letra do seu nome e {letra}
#         A ultima letra do seu nome e {Letra}
# Se nada for digitado em nome ou idade:
#     exiba "Desculpas, voce deixou campos vazios"


nome = input('Digite ser Nome e Sobrenome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome Contem espacos')
    else:
        print('Seu nome nao Contem espacos')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
else:
    print('Desculpe voce deixou campos vazios.')
