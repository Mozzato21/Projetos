import json
import os

def carregar_ficheiro(caminho):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Ficheiro não encontrado: {caminho}")
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

def buscar_resposta(pergunta, base_conhecimento):
    pergunta_lower = pergunta.lower()
    melhor_match = None
    max_score = 0

    for item in base_conhecimento:
        score = 0
        for palavra in item['palavras_chave']:
            if palavra in pergunta_lower:
                score += 1
        
        if score > max_score:
            max_score = score
            melhor_match = item

    if melhor_match and max_score > 0:
        resposta = (
            f"📌 Tópico: {melhor_match['topico']}\n\n"
            f"{melhor_match['conteudo']}\n\n"
            f"💡 Dica do InvestGuia: {melhor_match['recomendacao']}"
        )
        return resposta
    else:
        return (
            "Não disponho dessa informação na minha base de conhecimento. "
            "Para sua segurança, consulte um especialista certificado (CEA/CFP)."
        )

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, '..', 'data', 'base_conhecimento.json')
    prompt_path = os.path.join(base_path, 'system_prompt.txt')

    print("--- Inicializando o InvestGuia ---")
    try:
        base_conhecimento = json.loads(carregar_ficheiro(data_path))
        _ = carregar_ficheiro(prompt_path)
        print("✅ Base de conhecimento e System Prompt carregados com sucesso!\n")
    except Exception as e:
        print(f"❌ Erro ao carregar ficheiros: {e}")
        return

    print("==================================================================")
    print(" Olá! Sou o InvestGuia, seu assistente de investimentos.")
    print(" Pergunte-me sobre SELIC, CDB, FGC, Reserva de Emergência, etc.")
    print(" Digite 'sair' para encerrar a conversa.")
    print("==================================================================\n")

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("\nInvestGuia: Bons investimentos e até à próxima!")
            break
        
        if not user_input:
            continue

        resposta = buscar_resposta(user_input, base_conhecimento)
        print(f"\nInvestGuia:\n{resposta}\n")
        print("-" * 65)

if __name__ == "__main__":
    main()
