### Catálago de Contatos - API RESTful
git clone https://github.com/samuelsouzato/aionscorp-python-challenge.git

## Visão Geral

Este projeto é uma API RESTful para gerenciar um catálogo de contatos, desenvolvida com FastAPI, SQLite e SQLAlchemy. Permite criar, listar, atualizar e excluir contatos com campos como nome, email, telefone e tags.

A API oferece suporte a paginação e filtragem por tags na listagem de contatos, além de validação de dados usando Pydantic.

## Tecnologias Utilizadas

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic (validação)
- Pytest (testes)
- Alembic (para migrações de banco)

Embora o desafio não tenha solicitado explicitamente o uso de uma ferramenta de migração, optei por incluir o Alembic para:

- Facilitar a manutenção e evolução do esquema do banco.
- Garantir que alterações futuras possam ser aplicadas sem perder dados ou precisar recriar o banco do zero.
- Permite aplicar, reverter e versionar mudanças no banco de forma segura e organizada, melhorando a qualidade e sustentabilidade do projeto.



# Passo a Passo para rodar o Projeto

# 1. Criar o ambiente virtual: 
python -m venv venv

# 2. Ativar o ambiente virtual:
No Windows (PowerShell): .\venv\Scripts\Activate.ps1

No Windows (Prompt de Comando - cmd): venv\Scripts\activate.bat

No Linux/macOS (terminal bash/zsh): source venv/bin/activate

# 3. Atualizar o pip para a última versão:
python -m pip install --upgrade pip

# 4. Instalar as dependências do projeto:
pip install -r requirements.txt

# 5. Rodar a migration para criar o banco e as tabelas:
alembic upgrade head

# 6. Rodar a aplicação:
uvicorn app.main:app --reload




