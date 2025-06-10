# Relatório de Testes e Feedback

**Projeto:** Sistema de Gerenciamento de Biblioteca Digital
**Autor:** Barbara Roberta Marchinski
**Data:** 09 de Junho de 2025

## 1. Resumo dos Testes Realizados

Foram executados testes manuais para validar o comportamento de todas as funcionalidades do sistema, cobrindo cenários de sucesso e de erro. Os resultados confirmaram que o sistema se comporta como o esperado.

| Funcionalidade Testada | Cenário de Teste | Resultado Esperado | Resultado Obtido | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Adicionar Documento** | Usuário fornece um caminho de arquivo válido. | O arquivo é copiado para a pasta `/documentos`. | O arquivo foi copiado com sucesso e a mensagem de confirmação foi exibida. | ✅ OK |
| **Adicionar Documento** | Usuário fornece um caminho de arquivo inválido. | Sistema exibe uma mensagem de "Arquivo não encontrado". | O sistema exibiu a mensagem de erro esperada e retornou ao menu. | ✅ OK |
| **Listar por Tipo** | Pasta `/documentos` contém arquivos de tipos variados. | O sistema lista os arquivos agrupados por `.pdf`, `.epub`, etc. | A listagem foi exibida corretamente, agrupada por tipo. | ✅ OK |
| **Listar por Ano** | Pasta `/documentos` contém arquivos de anos variados. | O sistema lista os arquivos agrupados por `2022`, `2023`, etc. | A listagem foi exibida corretamente, agrupada por ano. | ✅ OK |
| **Renomear Documento** | Usuário tenta renomear um arquivo existente. | O nome do arquivo na pasta `/documentos` é alterado. | O arquivo foi renomeado com sucesso. | ✅ OK |
| **Remover Documento** | Usuário tenta remover um arquivo que não existe. | Sistema exibe a mensagem "Documento não encontrado". | O sistema exibiu a mensagem de erro esperada. | ✅ OK |
| **Navegação no Menu** | Usuário digita uma opção inválida (ex: '9' ou 'abc'). | Sistema exibe "Opção inválida" e mostra o menu novamente. | O comportamento foi exatamente o esperado. | ✅ OK |

## 2. Feedback Recebido (Simulação)

O sistema foi apresentado a um "usuário-chave" (simulação de um bibliotecário) para coletar feedback sobre a usabilidade.

* **Feedback de:** Simulação de Bibliotecário Chefe
* **Data do Feedback:** 09 de Junho de 2025

**Pontos levantados:**

1.  **Segurança na Remoção:** Foi sugerido adicionar um passo de confirmação (`Você tem certeza? [s/n]`) antes de remover um arquivo, para evitar exclusões acidentais.
2.  **Organização da Listagem:** Foi solicitado que a lista de documentos fosse exibida em ordem alfabética para facilitar a visualização.

## 3. Análise e Ações Tomadas

Com base no feedback recebido, as seguintes melhorias foram incorporadas ao projeto para aumentar a robustez e a usabilidade do sistema.

### Ação 1: Confirmação de Segurança ao Remover

* **Análise:** O feedback foi considerado extremamente válido, pois aumenta a segurança do sistema e previne a perda de dados.
* **Implementação:** O arquivo `src/main.py` foi modificado. Antes de chamar a função `remover_documento()`, o sistema agora pede uma confirmação ao usuário. A remoção só prossegue se o usuário digitar 's' ou 'S'. Esta alteração foi testada e funciona como esperado.

### Ação 2: Listagem em Ordem Alfabética

* **Análise:** A sugestão melhora significativamente a experiência do usuário, tornando as listas mais fáceis e rápidas de consultar.
* **Implementação:** Nos laços de repetição (`for`) responsáveis por exibir as listas no arquivo `src/main.py`, a função nativa `sorted()` foi aplicada à lista de arquivos. Isso garante que a exibição seja sempre em ordem alfabética, sem a necessidade de alterar a lógica principal no `gerenciador.py`.

## 4. Conclusão

Os testes confirmaram que as funcionalidades principais do sistema estão operando corretamente. O ciclo de feedback foi fundamental para identificar pontos de melhoria na segurança e na usabilidade, que foram implementados com sucesso. O sistema agora se encontra em um estado mais robusto e amigável ao usuário, pronto para ser utilizado no ambiente da biblioteca.