# Registro de Resolução de Conflito

**Data:** 10 de Abril de 2026
**Arquivo:** `tela_login.py`
**Branches envolvidas:** `guarda-dados` (via main) e `atualiza-projeto`

### 1. Descrição do Conflito
O conflito ocorreu na linha de definição do widget `btn_login`. Após o merge da branch `guarda-dados` na `main`, o código estabelecia uma identidade visual com duas cores. Ao tentar realizar o merge da branch `atualiza-projeto`, o GitHub Desktop identificou uma divergência, pois esta branch propunha uma paleta de cores diferente para o mesmo componente.

* **Versão na Main:** `bg="navy"`, `fg="white"`
* **Versão na Branch atualiza-projeto:** `bg="lightblue"`, `fg="gray"`

### 2. Resolução
A resolução foi realizada manualmente utilizando o editor Visual Studio Code. O conflito foi sanado através da análise das opções e remoção dos marcadores de conflito (`<<<<<<<`, `=======`, `>>>>>>>`).

### 3. Justificativa da Decisão
Optei por manter a versão original da branch `main` (`bg="navy"`, `fg="white"`). A escolha baseou-se em critérios de acessibilidade e contraste.

### 4. Procedimento Técnico
1. Sincronização do conflito via GitHub Desktop.
2. Edição manual do arquivo `tela_login.py`.
3. Execução de um commit pelo Desktop para finalizar o merge de resolução.
4. Push para o repositório.
