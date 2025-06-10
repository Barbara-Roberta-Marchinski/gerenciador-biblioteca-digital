# Como Contribuir

Ficamos felizes com seu interesse em contribuir para o projeto Gerenciador de Biblioteca Digital! Para garantir que o processo seja tranquilo para todos, por favor, siga as diretrizes abaixo.

## Reportando Bugs

Se você encontrar um bug, por favor, abra uma "Issue" no GitHub detalhando o problema. Inclua passos para reproduzir o erro, o que você esperava que acontecesse e o que de fato aconteceu.

## Sugerindo Melhorias

Sugestões são sempre bem-vindas! Você pode abrir uma "Issue" para discutir uma nova funcionalidade ou melhoria que gostaria de ver no projeto.

## O Fluxo de Contribuição

1.  **Faça um Fork do Repositório:**
    Clique no botão "Fork" no canto superior direito da página do repositório no GitHub para criar uma cópia na sua conta.

2.  **Clone o seu Fork:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/gerenciador-biblioteca-digital.git](https://github.com/SEU-USUARIO/gerenciador-biblioteca-digital.git)
    ```

3.  **Crie uma Nova Branch:**
    Navegue para o diretório do projeto e crie uma branch para trabalhar na sua nova funcionalidade:
    ```bash
    git checkout -b minha-nova-feature
    ```
    (Use um nome descritivo para a branch, como `corrige-bug-listagem` ou `adiciona-funcao-busca`).

4.  **Faça suas Alterações:**
    Escreva seu código, corrija bugs e implemente a nova funcionalidade.

5.  **Faça o Commit das Suas Alterações:**
    Adicione seus arquivos e faça o commit com uma mensagem clara, seguindo o padrão de "Conventional Commits":
    * `feat:` para novas funcionalidades.
    * `fix:` para correções de bugs.
    * `docs:` para alterações na documentação.
    * `style:` para formatação de código.
    * `refactor:` para refatoração de código sem alteração de funcionalidade.
    * `test:` para adição de testes.

    ```bash
    git add .
    git commit -m "feat: Adiciona funcionalidade de busca por autor"
    ```

6.  **Envie suas Alterações para o seu Fork:**
    ```bash
    git push origin minha-nova-feature
    ```

7.  **Abra um Pull Request (PR):**
    Vá para a página original do repositório no GitHub e clique em "New pull request". Descreva suas alterações em detalhes e submeta o PR para revisão.

Agradecemos sua contribuição!
