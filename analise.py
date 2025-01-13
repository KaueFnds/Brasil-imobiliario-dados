#imports 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregando os dados
dados_imobiliarios_br = pd.read_csv('Brasile-real-estate-dataset.csv', encoding='latin-1', index_col=0)

# Análise exploratória
print(dados_imobiliarios_br.head())
print(dados_imobiliarios_br.info())
print(dados_imobiliarios_br.describe())
print(dados_imobiliarios_br.isnull().sum())

# Distribuição de preço
sns.histplot(dados_imobiliarios_br['price_brl'], bins=30)
plt.show()

# Relação entre preço e área
sns.scatterplot(x='area_m2', y='price_brl', data=dados_imobiliarios_br)
plt.show()

# Relação entre preço por tipo de imovel 
sns.barplot(x='property_type', y='price_brl', data=dados_imobiliarios_br)
plt.show()

# Preço médio por estado 
sns.barplot(x='state', y='price_brl', data=dados_imobiliarios_br)
plt.xticks(rotation=45)
plt.show()

