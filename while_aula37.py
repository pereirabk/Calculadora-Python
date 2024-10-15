# Repetiçoes
# while(enquanto)
# Executa uma açao enquanto uma condiçao dor verdadeira
# Loop infinit -> Quando um codigo nao tem fim

contador = 0


"""while contador <= 100:
    contador +=  1

    if contador == 6:
        print('Nao vou mostrar o 6.0')
        continue

    if contador >= 10 and contador <= 27:
        print('Nao vou mostrar o', contador)
        continue

    print( contador)

    if contador == 40:
        break
"""

qtd_linhas = 50
qtd_colunas = 5

linha = 1 

while linha <= qtd_linhas:

    coluna = 1
    while coluna <= qtd_linhas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')



"""
condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome  == 'sair':
        break
    

print('Acabou bye bye!')"""