import ollama

def ask_model(prompt:str) -> str:
    try:
        resposta = ollama.chat(model="phi",messages=[{"role": "user","content": prompt}])

        return resposta["message"]["content"]
    except Exception as erro:
        return f"Erro ao chamar o modelo: {erro}"