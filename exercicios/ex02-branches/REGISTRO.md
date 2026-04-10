# Estrutura de Ramificação do Projeto (Git Flow)

Para a organização deste portfólio, adotei uma estratégia de branches baseada em funcionalidades específicas (Feature Branches), garantindo que a branch `main` permanecesse sempre estável.

## 🌳 Organização das Branches

### 1. Branch Principal (`main`)
- **Função:** Contém o código estável e finalizado.
- **Fluxo:** Recebe os merges das branches de funcionalidade após a validação e resolução de conflitos.

### 2. Branch de Integração dos Dados (`feat/guarda-dados`)
- **Objetivo:** Implementação da lógica de manipulação de arquivos `.txt`.
- **Alterações:** Criação das funções de leitura e escrita para salvar usuários no disco.

### 3. Branch de Interface (`feat/atualiza-projeto`)
- **Objetivo:** Melhorias de features e ajustes visuais.
- **Conflito:** Esta branch trazia a montagem dos arquivos de telas, e foi utilizada para gerar o conflito proposital com a branch de persistência ao alterar os mesmos componentes visuais na tela de login.

### 4. Branch de Documentação (`docs/configura-arquivos`)
- **Objetivo:** Registros de conflito, branches, commits e reflexão final.
- **Fluxo:** Última branch a ser integrada ao projeto antes da entrega.

### 5. Branch de Atualização do README (`docs/atualiza-readme`)
- **Objetivo:** Escrita do README.
- **Fluxo:** Mantém o arquivo README separado dos outros para manutenção mais fácil.

## 🛠️ Processo de Integração
O processo de integração seguiu o fluxo de Pull Requests (PRs), permitindo a revisão do código antes da mesclagem definitiva. Nos casos de divergência de código entre as branches de funcionalidade e a main, foi realizada a resolução manual de conflitos via terminal e VS Code.
