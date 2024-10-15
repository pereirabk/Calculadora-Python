# (Caractere) (><^)(quantidade)
# > - Esquerda
# < - Diretia
# ^ - Centro
# = - Forca o numero a aparecer antes dos Zeros
# Sinal - + ou - 
# ex.: 0>-100,. 1f
# Conversion flags - !r !s !a 


variavel = 'ABC'
print(f'{variavel:}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print('O hexadecimal de 1500 e {1500:08X}')
print(f'{variavel!r}')