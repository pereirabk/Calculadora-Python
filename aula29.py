numero_str =  input('Vou dobra o numero que voce digitar confia!: ' )


try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} e {numero_float * 2}')
except:
    print('Isso nao e um numero')





# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro do numero {numero_str} e {numero_float * 2:.0f}')
# else:
#     print('Isso nao e um numero')