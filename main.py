import json
import os

ARQUIVO_LIVROS = "livros.json"


def carregar_livros():
    if os.path.exists(ARQUIVO_LIVROS):
        try:
            with open(ARQUIVO_LIVROS, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON. Será iniciada uma lista vazia.")
            return []
    return []


def salvar_livros(livros):
    with open(ARQUIVO_LIVROS, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)


def cadastrar_livro(livros):
    print("\n=== CADASTRAR LIVRO ===")
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()

    if not titulo or not autor:
        print("Título e autor são obrigatórios.")
        return

    livro = {
        "titulo": titulo,
        "autor": autor,
        "emprestado": False
    }

    livros.append(livro)
    salvar_livros(livros)
    print("Livro cadastrado com sucesso!")


def listar_livros(livros):
    print("\n=== LISTA DE LIVROS ===")

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for i, livro in enumerate(livros, start=1):
        status = "Emprestado" if livro["emprestado"] else "Disponível"
        print(f"{i}. Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {status}")


def buscar_livro(livros):
    print("\n=== BUSCAR LIVRO ===")
    busca = input("Digite o título do livro: ").strip().lower()

    encontrados = [
        livro for livro in livros
        if busca in livro["titulo"].lower()
    ]

    if not encontrados:
        print("Nenhum livro encontrado.")
        return

    print("\nLivros encontrados:")
    for i, livro in enumerate(encontrados, start=1):
        status = "Emprestado" if livro["emprestado"] else "Disponível"
        print(f"{i}. Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {status}")


def emprestar_livro(livros):
    print("\n=== EMPRESTAR LIVRO ===")
    listar_livros(livros)

    if not livros:
        return

    try:
        numero = int(input("Digite o número do livro que deseja emprestar: "))

        if numero < 1 or numero > len(livros):
            print("Número inválido.")
            return

        livro = livros[numero - 1]

        if livro["emprestado"]:
            print("Esse livro já está emprestado.")
        else:
            livro["emprestado"] = True
            salvar_livros(livros)
            print("Livro emprestado com sucesso!")

    except ValueError:
        print("Digite um número válido.")


def devolver_livro(livros):
    print("\n=== DEVOLVER LIVRO ===")
    listar_livros(livros)

    if not livros:
        return

    try:
        numero = int(input("Digite o número do livro que deseja devolver: "))

        if numero < 1 or numero > len(livros):
            print("Número inválido.")
            return

        livro = livros[numero - 1]

        if not livro["emprestado"]:
            print("Esse livro já está disponível.")
        else:
            livro["emprestado"] = False
            salvar_livros(livros)
            print("Livro devolvido com sucesso!")

    except ValueError:
        print("Digite um número válido.")


def remover_livro(livros):
    print("\n=== REMOVER LIVRO ===")
    listar_livros(livros)

    if not livros:
        return

    try:
        numero = int(input("Digite o número do livro que deseja remover: "))

        if numero < 1 or numero > len(livros):
            print("Número inválido.")
            return

        removido = livros.pop(numero - 1)
        salvar_livros(livros)
        print(f"Livro '{removido['titulo']}' removido com sucesso!")

    except ValueError:
        print("Digite um número válido.")


def menu():
    livros = carregar_livros()

    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro")
        print("4. Emprestar livro")
        print("5. Devolver livro")
        print("6. Remover livro")
        print("7. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            buscar_livro(livros)
        elif opcao == "4":
            emprestar_livro(livros)
        elif opcao == "5":
            devolver_livro(livros)
        elif opcao == "6":
            remover_livro(livros)
        elif opcao == "7":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()