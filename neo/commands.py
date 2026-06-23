### COMANDOS ####
from services.github_api import buscar_usuario, buscar_repositorios
from services.system_info import system_info
from services.java_api import consultar_java
from services.terminal_serv import execute_command
from services.python_api import consultar_python

def process_command(command):
    partes = command.split()

    if command == "status":
        return "Estamos ON no seu Sistema Operacional"

    elif command == "help":
        return """
           Esses são os meus comandos:
           - hello, eai, ola, oi -> Cumprimento
           - exit -> Encerro o programa
           - system -> Mostro dados básicos do seu sistema
           
           - java + <topico> -> Consulto informações no Stack Overflow sobre java
           
           === GITHUB ===
           - github + <username> -> Consulto o perfil do github que você informar.
           - repos + <username> -> Te dou detalhes de repositorios do usuario informado.
           """
    elif command == "system":
        return system_info()

    elif partes[0] == "terminal": ## aceita comandos shell
        if len(partes) < 2:
            return "Digite o comando que deseja executar"
        comando = " ".join(partes[1:])
        return execute_command(comando)

    elif partes[0] == "github":
        if len(partes) < 2:
            return "Digite um usuário GitHub"   ## para não quebrar
        username = partes[1]
        return buscar_usuario(username)

    elif partes[0] == "repos":
        if len(partes) < 2:
            return "Digite um usuário GitHub"
        username = partes[1]
        return buscar_repositorios(username)


    elif partes[0] == "java":
        if len(partes) < 2:
            return "Digite um tópico java"
        topico = " ".join(partes[1:])
        return consultar_java(topico)

    elif partes[0] == "python":
        if len(partes) < 2:
            return "Digite um tópico python"
        topico = " ".join(partes[1:])
        return consultar_python(topico)

    else:
        return "Não reconheço esse comando cara."