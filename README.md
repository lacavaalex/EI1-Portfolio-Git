# Portfólio Git — Desenvolvimento de Software (CIN0136)

Este repositório documenta minha evolução no uso de ferramentas de controle de versão, aplicando fluxos de trabalho profissionais, commits semânticos e gestão de conflitos.

**Aluno:** Alex Lacava
**Instituição:** CIn-UFPE
**Projeto Base:** Validador de E-mail em Python

---

## 🚀 Funcionalidades
- **Cadastro:** Registro de novos usuários com validação de formato de e-mail e tamanho de senha.
- **Persistência:** Os dados são salvos localmente em um arquivo `usuarios.txt`.
- **Login:** Autenticação real consultando o banco de dados em texto.
- **Navegação:** Fluxo completo entre telas (Cadastro -> Login -> Bem-Vindo).
- **Multiplataforma:** Código ajustado para rodar tanto em Linux (Debian) quanto em Windows.

## 📂 Estrutura do Repositório

- `tela_cadastro.py`: Interface para criação de contas.
- `tela_login.py`: Interface para autenticação.
- `tela_bem_vindo.py`: Dashboard de sucesso pós-login.
- `usuarios.txt`: Armazenamento local das credenciais (ignorado no .gitignore por segurança).
* `exercicios/ex01-commits/`: Práticas focadas em mensagens padronizadas.
* `exercicios/ex02-branches/`: Demonstração de fluxo paralelo.
* `exercicios/ex03-conflito/`: Registro detalhado da resolução de um merge conflict.
* `REFLEXAO.md`: Relato crítico sobre o processo de aprendizagem e ferramentas utilizadas.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Interface Gráfica:** Tkinter
- **Controle de Versão:** Git e GitHub Desktop


## 📝 Metodologia de Desenvolvimento
Foram aplicadas boas práticas de desenvolvimento, incluindo:
- **Commits Semânticos:** Uso de prefixos como `feat`, `fix`, `style` e `chore`.
- **Git Flow:** Trabalho com múltiplas branches (`feat/`, `docs/`) e Pull Requests com auto-review.
- **Resolução de Conflitos:** Demonstração de resolução manual de divergências de código.

---

## 🔧 Instalação de Dependências

Para executar este projeto no Linux (especificamente em distribuições baseadas no Debian), é necessário instalar o suporte ao Tkinter manualmente:

1. Atualize a lista de pacotes:
   ```bash
   sudo apt update
   
2. Instale o pacote do Tkinter:
    ```bash
   sudo apt install python3-tk

---