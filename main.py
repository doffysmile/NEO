#!/usr/bin/env python3
from neo.commands import process_command
from neo.memory import save_memory
from neo.brain import ask_model
from neo.custom import principal, erro, info
from colorama import Fore

info("Essa é a versão 0.0.5\n")

principal("Wake up.")
principal("Neo online")
principal("Waiting commands...\n")

print("Digite 'help' para ver meus comandos")

while True:
    ####  RECEBENDO INFOS COM MODELO OLLAMA
    user_input = input(Fore.GREEN + "Neo > ")
    if user_input == "exit":
        principal("Encerrando Neo")
        principal("Goodbye!")
        break
    comando = process_command(user_input)
    if comando is not None:
        print(comando)
    else:
        resposta = ask_model(user_input)
        print(resposta)
    save_memory(user_input)
