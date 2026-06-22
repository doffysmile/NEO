import platform
import os

def system_info():
    sistema = platform.system()
    kernel = platform.release()
    usuario = os.getlogin()

    return f"""
    === Informações do Sistema ===
    Sistema: {sistema}
    Kernel: {kernel}
    Usuario: {usuario}
    """