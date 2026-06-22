import requests

### API BÁSICA DO STACKE
def consultar_java(topico):
    url = "https://api.stackexchange.com/2.3/search"

    parametros = {
        "order": "desc",
        "sort": "votes",
        "tagged": "java",
        "intitle": topico,
        "site": "stackoverflow"
    }

    try:
        resposta = requests.get(url, params=parametros)
        resposta.raise_for_status()
        dados = resposta.json()
        perguntas = dados["items"][:3]

        if len(perguntas)== 0:
            return "Nada encontrado"

        primeira_pergunta = perguntas[0]
        titulo = primeira_pergunta["title"]
        link = primeira_pergunta["link"]

        return f"""
        ==== JAVA ====
        Tópico: {topico}
        Resultado mais relevante do Stack Overflow:
        
        Titulo: {titulo}
        Link: {link}
        
        """
    except requests.exceptions.RequestException as erro:
        return f"Erro na consulta : {erro}"