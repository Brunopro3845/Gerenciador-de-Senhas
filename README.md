# 🔐 Gerenciador de Senhas em Python

Um gerenciador de senhas desenvolvido em Python que permite gerar, armazenar, consultar e remover credenciais de forma simples através do terminal.

##  Sobre o Projeto

Este projeto foi criado com o objetivo de praticar conceitos fundamentais de Python, como manipulação de arquivos JSON, funções, estruturas de repetição, tratamento de exceções e organização de código.

O sistema permite armazenar informações de login para diferentes serviços, gerando senhas aleatórias automaticamente e salvando os dados localmente.

##  Funcionalidades

- ✅ Gerar senhas seguras automaticamente
- ✅ Salvar contas e credenciais
- ✅ Listar todas as contas cadastradas
- ✅ Buscar uma conta específica
- ✅ Remover contas salvas
- ✅ Armazenamento em arquivo JSON
- ✅ Criação automática do banco de dados local

## 🛠 Tecnologias Utilizadas

- Python 3
- JSON
- os
- random
- string

##  Estrutura do Projeto

```text
 Gerenciador-de-Senhas
┣  main.py
┣  senhas.json
┗  README.md
```

##  Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Brunopro3845/Gerenciador-de-Senhas.git
```

### 2. Entre na pasta do projeto

```bash
cd Gerenciador-de-Senhas
```

### 3. Execute o programa

```bash
python main.py
```

##  Exemplo de Uso

```text
===================================
   GERENCIADOR DE SENHAS
===================================

1 - Adicionar conta
2 - Listar contas
3 - Buscar conta
4 - Remover conta
0 - Sair

Escolha uma opção:
```

### Exemplo de Conta Salva

```json
{
    "github": {
        "usuario": "Bruno3845",
        "senha": "A@7mP!2xQ9#k"
    },
    "steam": {
        "usuario": "Bruno3845",
        "senha": "X#8kLp2@Q1"
    }
}
```

##  Objetivos de Aprendizado

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Funções
- Estruturas condicionais
- Estruturas de repetição
- Manipulação de arquivos
- Leitura e escrita em JSON
- Tratamento de exceções
- Organização de código
- Modularização básica

##  Limitações Atuais

Este projeto tem fins educacionais e ainda não implementa recursos avançados de segurança.

Atualmente:

- As senhas são armazenadas em texto simples.
- Não existe autenticação por senha mestra.
- Não há criptografia dos dados.

##  Melhorias Futuras

- [ ] Utilizar a biblioteca `secrets` para geração criptograficamente segura
- [ ] Implementar senha mestra
- [ ] Criptografar os dados com a biblioteca `cryptography`
- [ ] Adicionar cópia automática para a área de transferência
- [ ] Criar interface gráfica com Tkinter
- [ ] Adicionar edição de contas existentes
- [ ] Criar sistema de backup automático
- [ ] Adicionar pesquisa parcial por nome de serviço

##  Status do Projeto

🟢 Em desenvolvimento

##  Autor

**Bruno Miguel**

GitHub: :contentReference[oaicite:0]{index=0}

---

⭐ Se este projeto te ajudou ou serviu de inspiração, considere deixar uma estrela no repositório.
