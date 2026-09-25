from sklearn.preprocessing import StandardScaler

# Criar transformação logarítmica para suavizar assimetria de valores altos em Amount
df['Amount_Log'] = np.log1p(df['Amount'])

# Padronização de Time e Amount_Log
scaler = StandardScaler()
df['Scaled_Time'] = scaler.fit_transform(df[['Time']])
df['Scaled_Amount'] = scaler.fit_transform(df[['Amount_Log']])

# Remover colunas originais brutas
X = df.drop(columns=['Class', 'Time', 'Amount', 'Amount_Log'])
y = df['Class']
