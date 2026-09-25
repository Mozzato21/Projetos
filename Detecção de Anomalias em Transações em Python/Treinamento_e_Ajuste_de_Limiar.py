from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, precision_recall_curve, confusion_matrix

# Treinamento do XGBoost com peso de classe
scale_pos_weight = (len(y_train) - sum(y_train)) / sum(y_train)

xgb_model = XGBClassifier(
    scale_pos_weight=scale_pos_weight,
    random_state=42,
    eval_metric='logloss'
)
xgb_model.fit(X_train, y_train)

# Obter probabilidades de fraude
y_probs = xgb_model.predict_proba(X_test)[:, 1]

# Ajuste do limiar de decisão
custom_threshold = 0.3
y_pred_custom = (y_probs >= custom_threshold).astype(int)

print(f"--- Avaliação com Limiar Customizado ({custom_threshold}) ---")
print(classification_report(y_test, y_pred_custom))
