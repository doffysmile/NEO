Aqui um pequeno README para conectar o Neo ao seu computador.
Primeiramente RELEVE POIS É UMA VERSÃO 0.0.1 PILOTO

Neo é um agente, bem simples, que funciona no terminal.
Para iniciar ele na sua máquina você irá fazer o seguinte

1 - Descompactar (obvio)
2 - No terminal
    bash~ cd caminho/neo
    execute -> nano ~/.local/bin/neo
    verifique se o arquivo contém o seguinte:
    #!/bin/bash
    python3 /caminho/neo/main.py
    
    Se estiver tudo okay, faça -> CTRL + O, ENTER, CTRL + X, para salvar e   sair
3 - Execute -> bash~ chmod +x ~/.local/bin/neo
4 - Execute -> echo $PATH
    Deve retornar algo como home/user/.local/bin....
    Dessa forma o neo já estará pronto para ser usado, basta digitar 'neo' no seu terminal
    
    
5 - Caso não após executar echo $PATH, ele não retornar o caminho, faça o seguinte
5.1 - Execute novamente -> nano ~/.bashrc
        E ao final do arquivo escreva -> export PATH="$HOME/.local/bin:$PATH", CTRL + O, ENTER, CTRL + X, para salvar e   sair
5.2 - Execute -> source ~/.bashrc

Esses ultimos devem resolver.
        
