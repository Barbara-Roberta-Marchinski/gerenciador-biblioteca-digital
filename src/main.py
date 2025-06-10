from gerenciador import (
    listar_documentos_por_tipo,
    listar_documentos_por_ano,
    adicionar_documento,
    renomear_documento,
    remover_documento
)

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Sistema de Gerenciamento de Biblioteca Digital ---")
    print("1. Listar documentos por tipo")
    print("2. Listar documentos por ano")
    print("3. Adicionar documento")
    print("4. Renomear documento")
    print("5. Remover documento")
    print("6. Sair")
    return input("Escolha uma opção: ")

def main():
    """Função principal que executa a interface de linha de comando."""
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            docs = listar_documentos_por_tipo()
            for tipo, arquivos in docs.items():
                print(f"\nTipo: {tipo.upper()}")
                for arq in arquivos:
                    print(f"  - {arq}")
        
        elif opcao == '2':
            docs = listar_documentos_por_ano()
            for ano, arquivos in sorted(docs.items()):
                print(f"\nAno: {ano}")
                for arq in arquivos:
                    print(f"  - {arq}")

        elif opcao == '3':
            origem = input("Digite o caminho completo do arquivo a ser adicionado: ")
            novo_nome = input("Digite o novo nome do arquivo (padrão: ANO_Autor_Titulo.extensao): ")
            sucesso, msg = adicionar_documento(origem, novo_nome)
            print(msg)

        elif opcao == '4':
            nome_antigo = input("Digite o nome do arquivo a ser renomeado: ")
            nome_novo = input("Digite o novo nome para o arquivo: ")
            sucesso, msg = renomear_documento(nome_antigo, nome_novo)
            print(msg)

        elif opcao == '5':
            nome_arquivo = input("Digite o nome do arquivo a ser removido: ")
            sucesso, msg = remover_documento(nome_arquivo)
            print(msg)

        elif opcao == '6':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()