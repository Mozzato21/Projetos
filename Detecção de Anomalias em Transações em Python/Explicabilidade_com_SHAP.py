import shap

# Inicializar o explicador baseado em árvores
explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)

# Gráfico de impacto geral das variáveis
shap.summary_plot(shap_values, X_test)

# Explicar uma transação específica identificada como fraude
fraude_idx = np.where((y_test == 1) & (y_pred_custom == 1))[0][0]
shap.force_plot(
    explainer.expected_value, 
    shap_values[fraude_idx], 
    X_test.iloc[fraude_idx],
    matplotlib=True
)
