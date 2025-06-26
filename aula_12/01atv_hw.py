#  primeiro declara que pe pra importar da bib pandas quandofor chamado pd
import pandas as pd

#criação da lista com as quantidades e os diferentes produtos em estoque
produtos = ['notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Camera']
quantidade_estoque = [15, 30, 20, 10, 25]

#criar a serie - declarar variável
estoque = pd.series(quantidade_estoque, index=produtos)

#exibe a serie
print("Série Estoque de Produtos: ")
print(estoque)