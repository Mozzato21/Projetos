from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Fraudes no Treino: {y_train.sum()} ({y_train.mean():.4%})")
print(f"Fraudes no Teste: {y_test.sum()} ({y_test.mean():.4%})")
