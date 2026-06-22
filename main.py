#!/usr/bin/env python3
from neo.commands import process_command
from neo.memory import save_memory

print("Essa é a versão 0.0.1\n")

print("Wake up.")
print("Neo online")
print("Waiting commands...\n")

print("Digite 'help' para ver meus comandos")

while True:
    ####  RECEBENDO INFOS
    user_input = input("Neo > ")

    if user_input == "exit":
        print("Encerrando Neo")
        break

    save_memory(user_input)

    resposta = process_command(user_input)
    print(resposta)
