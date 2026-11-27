# NEO

*Wake up, Neo...*

*The Matrix has you...*

*Follow the white rabbit.*

---

**Assistente pessoal | Inteligência artificial local | Interface de terminal**

## Sobre o projeto

O NEO é um assistente pessoal de propósito técnico, desenvolvido em Python, com uma arquitetura modular e uma interface baseada em terminal.

O projeto busca integrar inteligência artificial local, serviços do sistema operacional, APIs externas e mecanismos de memória persistente em um único ambiente.

A identidade visual é inspirada no universo de Matrix, preservando a estética clássica dos terminais.

## Funcionalidades

- Interface de terminal desenvolvida com Rich.
- Identidade visual personalizada.
- Integração com modelos locais de inteligência artificial através do Ollama.
- Consulta de informações do sistema operacional.
- Execução de comandos no terminal.
- Consulta de perfis e repositórios do GitHub.
- Pesquisa de informações técnicas sobre Java e Python através do Stack Overflow.
- Persistência do histórico de comandos.
- Renderização de respostas em Markdown.
- Configuração do modelo de inteligência artificial por variável de ambiente.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal de desenvolvimento |
| Rich | Interface e renderização no terminal |
| Ollama | Integração com modelos locais de IA |
| Requests | Requisições HTTP e integração com APIs |
| Psutil | Dependência para monitoramento do sistema |
| JSON Lines | Persistência do histórico de comandos |
| Git | Controle de versão |
| GitHub | Hospedagem do repositório |

## Arquitetura

O NEO adota uma arquitetura modular, buscando estabelecer uma separação de responsabilidades entre a interface, o núcleo da aplicação, os serviços externos e os mecanismos de persistência.

```text
NEO/
├── neo/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── boot.py
│   │   ├── console.py
│   │   ├── prompt.py
│   │   ├── renderer.py
│   │   └── theme.py
│   ├── __init__.py
│   ├── brain.py
│   ├── commands.py
│   └── memory.py
├── services/
│   ├── __init__.py
│   ├── github_api.py
│   ├── java_api.py
│   ├── python_api.py
│   ├── system_info.py
│   └── terminal_serv.py
├── utils/
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### Responsabilidades dos módulos

| Módulo | Responsabilidade |
|---|---|
| `main.py` | Inicialização e fluxo principal da aplicação |
| `brain.py` | Comunicação com o modelo de inteligência artificial |
| `commands.py` | Identificação e direcionamento dos comandos internos |
| `memory.py` | Persistência do histórico de interações |
| `config/` | Configurações da aplicação |
| `ui/` | Interface, identidade visual e renderização |
| `services/` | Integração com serviços internos e externos |
| `utils/` | Recursos auxiliares |

## Instalação

### Pré-requisitos

- Python 3.14, versão utilizada no desenvolvimento.
- Git.
- Ollama, para utilização da inteligência artificial local.
- Um modelo de linguagem compatível.
- Sistema operacional Linux, ambiente utilizado no desenvolvimento.

### Clonagem do repositório

```bash
git clone -b desenvolvimento https://github.com/doffysmile/NEO.git
cd NEO
```

### Criação do ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Instalação das dependências

```bash
python -m pip install -r requirements.txt
```

### Configuração do Ollama

Caso o servidor Ollama não esteja em execução, inicialize-o em outro terminal:

```bash
ollama serve
```

Instale um modelo de linguagem:

```bash
ollama pull qwen2:1.5b
```

Para consultar os modelos disponíveis localmente:

```bash
ollama list
```

### Inicialização do NEO

```bash
python main.py
```

Para utilizar outro modelo previamente instalado:

```bash
NEO_MODEL=qwen3:8b python main.py
```

## Comandos disponíveis

| Comando | Descrição |
|---|---|
| `help` | Exibe os comandos disponíveis |
| `status` | Apresenta o estado da aplicação |
| `system` | Consulta informações do sistema operacional |
| `terminal <comando>` | Executa um comando no terminal |
| `github <usuario>` | Consulta um perfil do GitHub |
| `repos <usuario>` | Consulta os repositórios de um usuário |
| `java <topico>` | Pesquisa informações técnicas sobre Java |
| `python <topico>` | Pesquisa informações técnicas sobre Python |
| `exit` | Encerra a aplicação |

Entradas não reconhecidas como comandos internos são direcionadas ao modelo de inteligência artificial configurado.

## Segurança e privacidade

O NEO prioriza a utilização de modelos de inteligência artificial executados localmente, reduzindo a dependência de serviços externos de processamento de linguagem.

As funcionalidades que utilizam APIs externas necessitam de conexão com a internet e podem transmitir informações relacionadas às consultas realizadas.

Os comandos de terminal são executados com as permissões do usuário responsável pela execução da aplicação.

O histórico de comandos, ambientes virtuais, credenciais e arquivos específicos das ferramentas de desenvolvimento não devem ser incluídos no versionamento.


### Implementações planejadas

- [ ] Padronização visual dos serviços.
- [ ] Retorno de dados estruturados pelos serviços.
- [ ] Monitoramento avançado do sistema operacional.
- [ ] Gerenciamento de modelos locais.
- [ ] Aprimoramento do módulo cognitivo.
- [ ] Integração da inteligência artificial com os serviços internos.
- [ ] Implementação de memória persistente com SQLite.
- [ ] Gerenciamento do contexto das conversas.
- [ ] Aprimoramento do tratamento de exceções.
- [ ] Implementação de políticas de segurança.
- [ ] Implementação de testes automatizados.
- [ ] Documentação técnica.
- [ ] Histórico de versões através do CHANGELOG.

### Organização das branches

| Branch | Finalidade |
|---|---|
| `master` | Versões oficialmente publicadas |
| `desenvolvimento` | Desenvolvimento de novas funcionalidades e melhorias |

As novas versões serão definidas de acordo com a natureza e o impacto das alterações realizadas.

## Documentações de referência

- [Python](https://docs.python.org/3/)
- [Rich](https://rich.readthedocs.io/)
- [Ollama](https://ollama.com/)
- [Ollama Python](https://github.com/ollama/ollama-python)
- [Psutil](https://psutil.readthedocs.io/)
- [GitHub REST API](https://docs.github.com/en/rest)
- [Semantic Versioning](https://semver.org/lang/pt-BR/)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/)


GitHub: [doffysmile](https://github.com/doffysmile)
---

*Follow the white rabbit.*
