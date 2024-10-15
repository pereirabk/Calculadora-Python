entrada = input('Digite um numere: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero {entrada_int} é {par_impar_texto} ')
else:
    print('Voce nao digitou um numero inteito')