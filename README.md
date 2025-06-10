# Gerenciador de Biblioteca Digital

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## Descrição do Projeto
Este projeto é um sistema de gerenciamento de biblioteca digital desenvolvido em Python. Foi criado para resolver a necessidade de uma biblioteca universitária de gerenciar de forma eficiente sua vasta coleção de documentos digitais (artigos, teses, livros), substituindo um processo manual propenso a erros.

---

## Funcionalidades
O sistema oferece uma interface de linha de comando (CLI) para as seguintes operações:

* **Listar documentos:** Organizados por tipo de arquivo (PDF, ePub, etc.) ou por ano de publicação.
* **Adicionar documentos:** Copiar novos arquivos para o diretório da biblioteca.
* **Renomear documentos:** Alterar o nome de arquivos existentes.
* **Remover documentos:** Excluir arquivos da biblioteca de forma permanente.

---

## Tecnologias Utilizadas
* **Python 3:** Linguagem principal do projeto.
* **Git:** Sistema de controle de versão.
* **GitHub:** Plataforma de hospedagem e colaboração do projeto.

---

##  Como Executar o Projeto

Para executar o sistema em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Barbara-Roberta-Marchinski/gerenciador-biblioteca-digital.git](https://github.com/Barbara-Roberta-Marchinski/gerenciador-biblioteca-digital.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd gerenciador-biblioteca-digital
    ```

3.  **Crie e ative o ambiente virtual:**
    ```bash
    # Crie o ambiente
    python -m venv venv

    # Ative o ambiente (Windows)
    .\venv\Scripts\activate

    # Ative o ambiente (macOS/Linux)
    source venv/bin/activate
    ```

4.  **Execute o sistema:**
    ```bash
    python src/main.py
    ```

---

## Estrutura de Nomenclatura de Arquivos
Para que a funcionalidade de "Listar por Ano" funcione corretamente, os documentos adicionados à pasta `documentos/` devem seguir o padrão de nomenclatura:

**`ANO_Autor_Titulo.extensao`**

**Exemplo:** `2024_ClariceLispector_AHoradaEstrela.epub`

---

## Autor

Desenvolvido por Bárbara Roberta Marchinski.

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Barbara-Roberta-Marchinski)
