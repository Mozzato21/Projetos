# Detecção de Fraudes em Cartões de Crédito

## 1. Descrição do Problema
Este projeto aborda a identificação de transações fraudulentas em cartões de crédito utilizando dados reais transformados por PCA. O dataset possui um desbalanceamento extremo (0,17% de fraudes), tornando a acurácia tradicional uma métrica inadequada. O objetivo principal é maximizar o **Recall** da classe de fraude, minimizando o impacto financeiro de Falsos Negativos sem gerar um volume excessivo de Falsos Positivos.

## 2. Preparação dos Dados e Engenharia de Atributos
- **Escalonamento:** Acolhimento das variáveis `Time` e `Amount` com `StandardScaler` e transformação logarítmica em `Amount`.
- **Validação:** Divisão entre dados de treino (80%) e teste (20%) utilizando amostragem estratificada (`stratify=y`).
- **Técnicas de Balanceamento Testadas:** Comparação entre *Class Weight*, *Undersampling* (RandomUnderSampler) e *Oversampling* (SMOTE).

## 3. Comparação dos Modelos
Resultados da avaliação na classe de **Fraude (Classe 1)** na base de teste:

| Modelo | Tratamento | Limiar (Threshold) | Precisão | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Regressão Logística | Class Weight | 0.50 | 0.06 | 0.92 | 0.11 |
| Random Forest | Class Weight | 0.50 | 0.85 | 0.78 | 0.81 |
| XGBoost | scale_pos_weight | 0.30 | 0.82 | 0.86 | 0.84 |

## 4. Otimização do Limiar e Explicabilidade (SHAP)
- **Ajuste de Limiar:** A alteração do limiar de decisão do XGBoost para `0.30` permitiu elevar o Recall mantendo a precisão controlada.
- **Interpretação com SHAP:** As variáveis $V14$, $V12$, $V10$ e $V4$ apresentaram o maior impacto na tomada de decisão do modelo para classificar a transação como fraude.

## 5. Principais Evoluções em Relação à Solução Base
- Teste sistemático do tuning de limiar de decisão.
- Análise comparativa direta de desempenho entre SMOTE, Undersampling e Pesos de Classe nativos.
