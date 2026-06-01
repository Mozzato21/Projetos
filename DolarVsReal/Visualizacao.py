import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('USD_BRL_hist.csv', decimal='.')

# Conversão de DATA no formato DD.MM.YYYY
df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')

# Criação das colunas colunas Ano e Mês para formação de hierarquias e para agrupamentos
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month

# --------------------------------//-----------------------------------
# 1º: Visualização Temporal
# --------------------------------//-----------------------------------
plt.figure(figsize=(12, 5))
plt.plot(df['Data'], df['USD_BRL'], color='blue', linewidth=1)
plt.title('Evolução Diária da Cotação Dólar x Real (USD/BRL)')
plt.xlabel('Data')
plt.ylabel('Cotação (R$)')
plt.grid(True)
plt.show()

# --------------------------------//-----------------------------------
# 2°: Estatística Descritiva
# --------------------------------//-----------------------------------
# Agrupando a média anual da cotação
df_ano = df.groupby('Ano')['USD_BRL'].mean().reset_index()

plt.figure(figsize=(10, 5))
plt.bar(df_ano['Ano'].astype(str), df_ano['USD_BRL'], color='orange')
plt.title('Média Anual da Cotação (USD/BRL)')
plt.xlabel('Ano')
plt.ylabel('Cotação Média (R$)')
plt.show()

# --------------------------------//-----------------------------------
# 3°: Visualização Hierárquica
# --------------------------------//-----------------------------------
# Agrupando por Ano e Mês para criar a hierarquia
df_hierarquia = df.groupby(['Ano', 'Mes'])['USD_BRL'].mean().reset_index()
df_hierarquia['Ano'] = df_hierarquia['Ano'].astype(str)
df_hierarquia['Mes'] = df_hierarquia['Mes'].astype(str)

# Criando o Treemap
fig = px.treemap(
    df_hierarquia, 
    path=[px.Constant("Histórico de Cotações"), 'Ano', 'Mes'], 
    values='USD_BRL',
    color='USD_BRL',
    color_continuous_scale='RdBu',
    title='Treemap da Cotação Média Hierarquizada por Ano e Mês'
)
fig.write_html("treemap.html")
