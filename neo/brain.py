import ollama

SYSTEM_PROMPT = """
Você é NEO.
Seu nome é NEO.
Responda em português do Brasil.
Seja objetivo.
Seu estilo é futurista e técnico.
Exemplo:
"Entendido."
"Solicitação processada."
"Analisando informação..."
"""

conversation = [{"role": "system","content": SYSTEM_PROMPT}]
def ask_model(prompt: str):
    global conversation
    conversation.append({"role": "user","content": prompt})

    resposta = ollama.chat(model="qwen2:1.5b",messages=conversation)
    answer = resposta["message"]["content"]

    conversation.append({ "role": "assistant","content": answer})

    return answer