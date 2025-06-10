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
            if not docs:
                print("\nNenhum documento encontrado.")
            else:
                # --- MELHORIA 2: Ordena os tipos de arquivo (epub, pdf, etc.) ---
                for tipo in sorted(docs.keys()):
                    arquivos = docs[tipo]
                    print(f"\nTipo: {tipo.upper()}")
                    # --- MELHORIA 2: Ordena os arquivos de cada tipo em ordem alfabética ---
                    for arq in sorted(arquivos):
                        print(f"  - {arq}")
        
        elif opcao == '2':
            docs = listar_documentos_por_ano()
            if not docs:
                print("\nNenhum documento encontrado.")
            else:
                # --- MELHORIA 2: Ordena os anos ---
                for ano in sorted(docs.keys()):
                    arquivos = docs[ano]
                    print(f"\nAno: {ano}")
                    # --- MELHORIA 2: Ordena os arquivos de cada ano em ordem alfabética ---
                    for arq in sorted(arquivos):
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
            
            # --- MELHORIA 1: Adiciona confirmação antes de remover ---
            confirmacao = input(f"Tem certeza que deseja remover o arquivo '{nome_arquivo}'? Esta ação não pode ser desfeita. [s/n]: ")
            
            if confirmacao.lower() == 's':
                sucesso, msg = remover_documento(nome_arquivo)
                print(msg)
            else:
                print("Operação de remoção cancelada.")
            # --- FIM DA MELHORIA 1 ---

        elif opcao == '6':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()