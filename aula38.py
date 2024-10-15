"""
Interando String com while
"""

# ..... 0123456789 
nome = 'Brunno Kelvin'  # Interaveis

tamanho_nome = len(nome)  


indice = 0
novo_nome = ''
while indice < len(nome):

   letra = nome [indice]
   novo_nome += f'*{letra}'

   indice += 1

novo_nome += '*'
print(novo_nome)