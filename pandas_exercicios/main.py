import pandas as pd
import numpy as np

df_vendas = pd.read_csv("vendas_tech.csv", low_memory=False)
print(df_vendas)
df_gerentes = pd.read_excel("gerentes_lojas.xlsx")
print(df_gerentes)