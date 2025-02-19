import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    raise RuntimeError("Erro ao conectar ao banco de dados}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def test_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print(" Conexão com o banco de dados bem-sucedida!")
    except Exception as e:
        print( "Erro ao conectar ao banco de dados:")
        print(e) # Imprime o erro específico para ajudar na depuração
    finally:
        db.close()

# test connection
test_connection()