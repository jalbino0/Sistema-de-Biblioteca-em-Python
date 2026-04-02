# Sistema de Biblioteca em Python

Aplicação desenvolvida em **Python** que simula um sistema de gerenciamento de biblioteca, permitindo cadastrar, listar, buscar, emprestar, devolver e remover livros.

O objetivo do projeto é praticar conceitos fundamentais de programação, como estruturas de repetição, condicionais, funções, manipulação de arquivos e organização de dados em formato **JSON**.

---

# Sobre o Projeto

O **Sistema de Biblioteca em Python** foi criado com a proposta de simular o funcionamento básico de uma biblioteca, permitindo o controle de livros de forma simples pelo terminal.

Com o sistema, o usuário pode gerenciar os livros cadastrados, verificar quais estão disponíveis ou emprestados e atualizar essas informações de forma prática.

O projeto foi pensado como uma forma de aplicar, na prática, conteúdos importantes do curso de **Ciência da Computação**, especialmente relacionados à lógica de programação e manipulação de dados.

Com a aplicação, é possível:

- cadastrar novos livros  
- listar todos os livros cadastrados  
- buscar livros pelo título  
- emprestar livros  
- devolver livros  
- remover livros do sistema  

Assim, o projeto simula um pequeno sistema real de gerenciamento, ajudando no aprendizado de programação em Python.

---

# Repositório do Projeto

https://github.com/jalbino0/Sistema-de-Biblioteca-em-Python

---

# Objetivo do Sistema

O sistema foi desenvolvido para representar a operação de controle de livros em uma biblioteca.

A proposta é permitir uma organização simples dos livros cadastrados, facilitando ações como:

- registro de novos livros  
- consulta de livros disponíveis  
- controle de empréstimos  
- devolução de livros  
- remoção de registros  

Esse tipo de aplicação pode ser adaptado futuramente para bibliotecas escolares, pessoais ou acadêmicas.

---

# Funcionalidades Implementadas

## Cadastro de Livros
- Cadastro de título e autor
- Armazenamento das informações em arquivo JSON

## Listagem de Livros
- Exibição de todos os livros cadastrados
- Indicação do status de cada livro

## Busca de Livros
- Busca por título
- Exibição dos livros encontrados

## Empréstimo de Livros
- Alteração do status para emprestado
- Verificação de disponibilidade

## Devolução de Livros
- Alteração do status para disponível
- Controle simples de retorno

## Remoção de Livros
- Exclusão de livros cadastrados no sistema

---

# Demonstração do Sistema

O sistema funciona via terminal e apresenta um menu com as opções disponíveis para gerenciamento da biblioteca.

Exemplo de operações realizadas no sistema:

- cadastro de livros  
- listagem dos livros cadastrados  
- busca por título  
- empréstimo de livro  
- devolução de livro  
- remoção de livro  

---

# Integrante

- João Pedro de Moura Albino

---

# Como Rodar o Projeto

## Pré-requisitos

- Python 3 instalado na máquina

---

## Clonar o repositório

```bash
git clone https://github.com/seu-usuario/biblioteca-python.git
```

Entrar na pasta do projeto:

```bash
cd biblioteca-python
```

Executar o sistema:

```bash
python main.py
```

---

# Estrutura do Projeto

```bash
biblioteca-python/
├── main.py
├── livros.json
└── requirements.txt
```

Descrição da estrutura:

- `main.py` → arquivo principal com toda a lógica do sistema
- `livros.json` → arquivo utilizado para armazenar os dados dos livros
- `requirements.txt` → arquivo de dependências do projeto

---

# Funcionamento do Sistema

O sistema utiliza um menu interativo no terminal para que o usuário escolha as operações desejadas.

As opções disponíveis são:

```text
1. Cadastrar livro
2. Listar livros
3. Buscar livro
4. Emprestar livro
5. Devolver livro
6. Remover livro
7. Sair
```

Cada operação realiza uma ação específica sobre a lista de livros armazenada no arquivo JSON.

---

# Manipulação de Dados

O projeto utiliza o arquivo:

```bash
livros.json
```

Esse arquivo é responsável por armazenar os livros cadastrados, contendo informações como:

- título  
- autor  
- status de empréstimo  

Exemplo de estrutura de um livro no JSON:

```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "emprestado": false
}
```

---

# Conceitos Utilizados

O projeto foi desenvolvido com foco em conceitos básicos e intermediários de Python, como:

- funções  
- listas  
- dicionários  
- estruturas condicionais  
- estruturas de repetição  
- tratamento de erros  
- leitura e escrita em arquivos  
- manipulação de JSON  

---

# Interface do Sistema

A aplicação possui interface em modo texto, funcionando diretamente no terminal.

Principais características:

- menu simples e intuitivo  
- navegação por opções numéricas  
- mensagens de confirmação e erro  
- organização prática para uso básico  

---

# Melhorias Futuras

- cadastro de usuário responsável pelo empréstimo  
- registro da data de empréstimo e devolução  
- separação do código em múltiplos arquivos  
- uso de programação orientada a objetos  
- criação de interface gráfica  
- integração com banco de dados  

---

# Tecnologias Utilizadas

- Python  
- JSON  

---

# Licença

Projeto desenvolvido para fins acadêmicos e de aprendizado.
