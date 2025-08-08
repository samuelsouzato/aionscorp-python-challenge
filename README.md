# aionscorp-python-challenge

# PASSO A PASSO PARA RODAR O PROJETO

# 1. Criar o ambiente virtual: 
python -m venv venv

# 2. Ativar o ambiente virtual:
No Windows (PowerShell): .\venv\Scripts\Activate.ps1

No Windows (Prompt de Comando - cmd): venv\Scripts\activate.bat

No Linux/macOS (terminal bash/zsh): source venv/bin/activate

# 3. Atualizar o pip para a última versão:
pip install --upgrade pip

# 4. Instalar as dependências do projeto:
pip install -r requirements.txt

# 5. Rodar a migration para criar o banco e as tabelas:
alembic upgrade head

# 6. Rodar a aplicação:
uvicorn app.main:app --reload




