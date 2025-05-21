import pandas as pd

produtos = ['Noteb', 'Smartp', 'Tabl', 'Smartw', 'Cam']
quantdade_estoque = [15, 30, 20, 10, 25]

estoque = pd.Series(quantdade_estoque, index=produtos)

print('Série Estoque de Produtos: ')
print(estoque)
#  valor específico pelo indice
print('\nQuantidade de notebooks em estoque: ')
print(estoque['Noteb'])
#  selecionando multiplos valores
print('\nEstoque de Notebook e Câmera: ')
print(estoque[['Noteb', 'Cam']].values)

# filtrando produtos com estoque abaixoo de 20
print('\nProdutos com estoque abaixo de 20 unidades: ')
print(estoque[estoque < 20])

# op aritimetica: aumentar estoque em 5 unidades

print('aumentando estoque em 5 unidades para todos os produtos: ')
print(estoque + 5)

#incluindo um valor nulo para simular a falta de dados
estoque.loc['Headphone'] = None
print("\nEstoque com um valor nulo (Headphone): ")
print(estoque)

#op artm entre series
#CRIANDO OUTRA SERIE COM PREÇOS DOS PRODUTOS
precos = pd.Series([3500, 2500, 2500, 1200, 900], index=produtos)

print("\nValor total do estoque por produto(preço * quantidade): ")
print(precos * estoque)