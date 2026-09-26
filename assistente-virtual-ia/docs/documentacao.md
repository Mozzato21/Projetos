# 📚 Documentação do Projeto: InvestGuia

## 1. Definição do Agente
O **InvestGuia** é um assistente virtual voltado para a educação financeira básica e orientação sobre perfis de risco e produtos de investimento. O seu objetivo é desmistificar conceitos do mercado e auxiliar utilizadores a darem os primeiros passos com segurança.

## 2. Base de Conhecimento
A base encontra-se em `data/base_conhecimento.json` e cobre 12 tópicos essenciais:
- Conceitos essenciais: SELIC, CDI, Liquidez Diária vs. Vencimento, Inflação/IPCA.
- Produtos e Garantias: CDB, LCI/LCA, Tesouro Direto, Fundos Imobiliários (FIIs), FGC.
- Estratégias e Perfis: Reserva de Emergência, Diversificação, Perfis de Risco (Conservador, Moderado, Arrojado).

## 3. Prompts do Agente
O prompt do sistema (`src/system_prompt.txt`) garante que a IA:
- Atue como um educador financeiro responsável.
- Responda apenas com dados verificados da base de conhecimento.
- Recuse dar recomendações sobre tópicos não catalogados para evitar alucinações.

## 4. Aplicação Funcional
A aplicação (`src/app.py`) é executada localmente em Python via Terminal. Utiliza um algoritmo de pesquisa e correspondência de palavras-chave para recuperar a resposta exata e a dica prática correspondente.

## 5. Avaliação e Métricas
Para avaliar a qualidade das respostas, foram testados 3 cenários:
1. **Pergunta Direta ("O que é Selic?"):** Retornou o conceito exato com precisão total.
2. **Pergunta de Perfil ("Sou conservador, onde invisto?"):** Identificou o perfil e recomendou Tesouro Selic e CDB de liquidez diária.
3. **Pergunta Fora do Escopo ("Qual a melhor criptomoeda?"):** Ativou a trava de segurança e orientou a consulta a um especialista certificado.

## 6. Pitch do Projeto
O pitch resumido encontra-se no ficheiro `docs/pitch.md`.
