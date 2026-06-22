import subprocess
def execute_command(command):
    try:
        resultado = subprocess.check_output(command, shell=True, text=True)
        return resultado
    except subprocess.CalledProcessError as erro:
        return f"Erro ao executar o comando: {erro}"