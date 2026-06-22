import requests

def buscar_usuario(usuario):
    url = f"https://api.github.com/users/{usuario}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return f"""=== INFO PERFIL GITHUB ===\n
        Usuário: {dados["login"]}
        Repositorios públicos: {dados["public_repos"]}
        Criado em: {dados["created_at"]}
        """
    except requests.exceptions.RequestException as erro:
        return f"Erro : {erro}"


def buscar_repositorios(usuario):
    url = f"https://api.github.com/users/{usuario}/repos"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        texto = "=== Seus Repositorios ===\n"
        for repo in dados:
            texto = texto + f"| {repo['name']} |-> {repo['description']}\n"
        return texto
    except requests.exceptions.RequestException as erro:
        return f"Erro : {erro}"