import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento do dataset via link direto
url = "https://raw.githubusercontent.com/datasets/credit-card-fraud/main/data/creditcard.csv"
# Alternativa: link direto do Kaggle / S3 mantido no desafio
df = pd.read_csv(url)

# Checagem da proporção de classes
print("Distribuição das Classes:")
print(df['Class'].value_counts(normalize=True) * 100)

# Visualização do desbalanceamento
sns.countplot(x='Class', data=df)
plt.title('Distribuição de Transações (0: Legítima | 1: Fraude)')
plt.show()
