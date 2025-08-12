### Catálago de Contatos - API RESTful
git clone https://github.com/samuelsouzato/aionscorp-python-challenge.git

## Visão Geral

Este projeto é uma API RESTful para gerenciar um catálogo de contatos, desenvolvido com FastAPI, SQLite e SQLAlchemy. Permite criar, listar, atualizar e excluir contatos com campos: nome, email, telefone e tags.

A API oferece suporte a paginação e filtragem por tags na listagem de contatos, além de validação de dados usando Pydantic.

## Tecnologias Utilizadas

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic (validação)
- Pytest (testes)

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

# 5. Instalar extensão no VScode para visualizar tabelas no banco:
SQLite Viewer

# 6. Rodar a aplicação:
uvicorn app.main:app --reload

# 7. Documentação interativa da API

Após iniciar o servidor, as docs automáticas do FastAPI ficam em:

Swagger UI: http://127.0.0.1:8000/docs

## Passo a Passo para rodar os testes

# 1. Rodar todos os testes:

pytest -v

# 2. Rodar um arquivo de teste específico:

pytest tests/services/test_contato_create.py

# 3. Medir cobertura

pytest --cov=app 

