from app.models.contato import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():

    try:
        # Abrindo sessão conectada ao banco (engine)
        Session= sessionmaker(bind=db)
        session = Session()
        
        # independente do erro fecha
    finally: 
        session.close()