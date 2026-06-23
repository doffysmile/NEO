#!/usr/bin/env python3
from neo.commands import process_command
from neo.memory import save_memory
from neo.brain import ask_model

print("Essa é a versão 0.0.5\n")

print("Wake up.")
print("Neo online")
print("Waiting commands...\n")

print("Digite 'help' para ver meus comandos")

while True:
    ####  RECEBENDO INFOS COM MODELO OLLAMA
    user_input = input("Neo > ")
    if user_input == "exit":
        print("Encerrando Neo")
        print("Goodbye!")
        break
    comando = process_command(user_input)
    if comando is not None:
        resposta = comando
    else:
        resposta = ask_model(user_input)
        print(resposta)
    save_memory(user_input)
