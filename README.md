### 📇 Catálogo de Contatos - API RESTful

## Visão Geral

Este projeto é uma **API RESTful** desenvolvida com **FastAPI**, **SQLite** e **SQLAlchemy**, seguindo **arquitetura MVC adaptada para APIs REST**.  
Permite criar, listar, atualizar e excluir contatos com suporte a **paginação**, **filtragem por tags** e **validação de dados** com **Pydantic**.


## 📂 Estrutura do Projeto

```
app/
│
├── controllers/   
│   └── contato_controller.py  # Camada de controle: recebe dados das rotas, aplica regras de negócio,
│                              # chama os serviços correspondentes e retorna respostas tratadas.
│
├── database/
│   ├── database.py            # Configuração e inicialização da conexão com o banco de dados (SQLAlchemy).
│   ├── models.py              # Definição das tabelas e entidades do banco de dados usando ORM.
│   └── schema.py              # Modelos Pydantic para validação e serialização dos dados recebidos/enviados.
│
├── routes/
│   └── routes.py              # Definição dos endpoints da API (FastAPI APIRouter), mapeando métodos HTTP
│                              # para funções do controller.
│
├── services/
│   ├── contato_create.py      # Serviço responsável por criar contatos no banco.
│   ├── contato_delete.py      # Serviço responsável por excluir contatos no banco.
│   ├── contato_get.py         # Serviço responsável por listar ou buscar contatos.
│   └── contato_update.py      # Serviço responsável por atualizar dados de um contato.
│                              
│
├── tests/
│   ├── database/
│   │   └── test_schema.py     #Testa a validação do schema ContactCreate com dados inválidos.
│   │
│   ├── routes/
│   │   └── test_routes.py     # Testes de integração para garantir que as rotas da API funcionem.
│   │
│   └── services/
│       ├── test_contato_create.py # Testa a criação de contatos (serviço).
│       ├── test_contato_delete.py # Testa a exclusão de contatos (serviço).
│       ├── test_contato_get.py    # Testa a listagem/busca de contatos (serviço).
│       └── test_contato_update.py # Testa a atualização de contatos (serviço).
│
└── main.py                    # Ponto de entrada da aplicação.
                               # Cria a instância FastAPI, registra rotas e configurações iniciais.

```

## Tecnologias Utilizadas

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic (validação)
- Pytest (testes)

# Como Executar

# 1. Criar o ambiente virtual: 
```bash
python -m venv venv
```
# 2. Ativar o ambiente virtual:

- Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

- Windows (Prompt de Comando - cmd): 
```bash
venv\Scripts\activate.bat
```

- Linux/macOS (terminal bash/zsh): 
```bash
source venv/bin/activate
```

# 3. Atualizar o pip para a última versão:
```bash
python -m pip install --upgrade pip
```
# 4. Instalar as dependências do projeto:
```bash
pip install -r requirements.txt
```
# 5. Rodar a aplicação:
```bash
uvicorn app.main:app --reload
```
# 6. Documentação interativa da API

- Após iniciar o servidor, as docs do FastAPI ficam em:

- Copie e cole na barra de pesquisa do seu navegador ou Ctrl + clique

- Swagger UI: http://127.0.0.1:8000/docs
## OBS: após inicar o servidor, será necessario abrir um novo terminal, volte paro opasso 2 e ative novamente o ambiemte virtual!!

# 7. Criar contato:

- Clique no endpoint /contato_create 
- Clique no botão "Try it out"

Você verá algo como: 
{
  "nome": "string",
  "telefone": "string",
  "email": "string",
  "tags": "string"
}

- Altere "String" da forma que desejar.. ex:

{
  "nome": "nome do contato",
  "telefone": "00000000000",
  "email": "seuemail@gmail.com",
  "tags": "familia"
}

- Clique no botão "Execute"
- Descendo mais um pouco você verá a mensagem "Contato criado com sucesso!"

# 8. Instalar extensão no VScode para visualizar tabela (contatos) no arquivo banco.db:
SQLite Viewer

# 9. Listar Contatos (todos ou por tags)
 
- Clique no endpoint /contato_list
- Clique no botão "Try it out"

- Clique no campo "Filtrar por tag" e adicione uma tag. ex: casa -> OPCIONAL
- Clique no campo "Número da página" e coloque o número da página mínima(1) e máxima(100)
- Clique no botão "Execute"
- Descendo mais um pouco você verá a lista de contatos cadastrados

# 10. Buscar contato por ID

- Clique no endpoint GET /{contato_id}
- Clique no botão "Try it out"
- Clique no campo "contato_id" e adicione o ID que deseja buscar. ex: 1
- Clique no botão "Execute"
- Descendo mais um pouco você verá o contato com o ID desejado.

# 11. Atualizar contato por ID

- Clique no endpoint PUT /{contato_id}
- Clique no botão "Try it out"
- Clique no campo "contato_id" e adicione o ID que deseja atualizar. ex: 1

Você verá algo como: 
{
  "nome": "string",
  "telefone": "string",
  "email": "string",
  "tags": "string"
}

- Altere os campos "String" para atualizar o contato desejado.
- Clique no botão "Execute"
- Descendo mais um pouco você verá a mensagem contato "Contato atualizado com sucesso!" com as informações atualizadas.
- Se você voltar no passo 11 e buscar o ID novamente, já estará com as informações atualizadas.

# 12. Deletar contato

- Clique no endpoint DELETE /{contato_id}
- Clique no botão "Try it out"
- Clique no campo "contato_id" e adicione o ID que deseja deletar. ex: 1
- Clique no botão "Execute"
- Descendo mais um pouco você verá a mensagem contato "Contato removido com sucesso!".

## Passo a Passo para rodar os testes

# 1. Rodar todos os testes feitos:
```bash
pytest -v
```
# 2. Rodar um arquivo de teste específico:

exemplo: 
```bash
pytest tests/services/test_contato_create.py
```
# 3. Medir cobertura:
```bash
pytest --cov=app 
```
