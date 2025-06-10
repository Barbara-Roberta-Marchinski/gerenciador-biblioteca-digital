import os
import shutil

# Caminho para a pasta onde os documentos estão armazenados.
# O '..' sobe um nível para sair de 'src' e depois entra em 'documentos'.
DIRETORIO_DOCUMENTOS = os.path.join(os.path.dirname(__file__), '..', 'documentos')

def listar_documentos_por_tipo():
    """Lista documentos agrupados por extensão (tipo de arquivo)."""
    documentos_por_tipo = {}
    if not os.path.exists(DIRETORIO_DOCUMENTOS):
        print("Diretório de documentos não encontrado.")
        return {}

    for nome_arquivo in os.listdir(DIRETORIO_DOCUMENTOS):
        if os.path.isfile(os.path.join(DIRETORIO_DOCUMENTOS, nome_arquivo)):
            # Pega a extensão do arquivo (ex: 'pdf', 'epub')
            tipo_arquivo = nome_arquivo.split('.')[-1]
            if tipo_arquivo not in documentos_por_tipo:
                documentos_por_tipo[tipo_arquivo] = []
            documentos_por_tipo[tipo_arquivo].append(nome_arquivo)
    
    return documentos_por_tipo

def listar_documentos_por_ano():
    """Lista documentos agrupados por ano de publicação, baseado no nome do arquivo."""
    documentos_por_ano = {}
    if not os.path.exists(DIRETORIO_DOCUMENTOS):
        print("Diretório de documentos não encontrado.")
        return {}
        
    for nome_arquivo in os.listdir(DIRETORIO_DOCUMENTOS):
        if os.path.isfile(os.path.join(DIRETORIO_DOCUMENTOS, nome_arquivo)):
            try:
                # Pega o ano do nome do arquivo (ex: '2023_...')
                ano = nome_arquivo.split('_')[0]
                if ano.isdigit():
                    if ano not in documentos_por_ano:
                        documentos_por_ano[ano] = []
                    documentos_por_ano[ano].append(nome_arquivo)
            except IndexError:
                # Ignora arquivos que não seguem o padrão de nomenclatura
                print(f"Aviso: O arquivo '{nome_arquivo}' não segue o padrão 'ANO_Autor_Titulo.extensao' e será ignorado na listagem por ano.")
                
    return documentos_por_ano

def adicionar_documento(caminho_origem, novo_nome_arquivo):
    """Adiciona um novo documento à biblioteca."""
    if not os.path.exists(caminho_origem):
        return False, "Arquivo de origem não encontrado."
    
    caminho_destino = os.path.join(DIRETORIO_DOCUMENTOS, novo_nome_arquivo)
    shutil.copy(caminho_origem, caminho_destino)
    return True, f"Documento '{novo_nome_arquivo}' adicionado com sucesso."

def renomear_documento(nome_antigo, nome_novo):
    """Renomeia um documento existente."""
    caminho_antigo = os.path.join(DIRETORIO_DOCUMENTOS, nome_antigo)
    if not os.path.exists(caminho_antigo):
        return False, "Documento não encontrado para renomear."
        
    caminho_novo = os.path.join(DIRETORIO_DOCUMENTOS, nome_novo)
    os.rename(caminho_antigo, caminho_novo)
    return True, f"Documento renomeado para '{nome_novo}'."

def remover_documento(nome_arquivo):
    """Remove um documento da biblioteca."""
    caminho_arquivo = os.path.join(DIRETORIO_DOCUMENTOS, nome_arquivo)
    if not os.path.exists(caminho_arquivo):
        return False, "Documento não encontrado para remover."
        
    os.remove(caminho_arquivo)
    return True, f"Documento '{nome_arquivo}' removido com sucesso."